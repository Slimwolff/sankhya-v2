from typing import Any, Callable, List
import json
from ..services.pesquisaPedidoLivroFiscal import pesquisaPedidoLivroFiscal
from ..services.processarNotaArquivo import processarNotaArquivo
from ..services.actionButton import actionButton
from ..services.Query import Query
from ..services.removePedidoLivroFiscal import removePedidoLivroFiscal
from ..services.validaXMLNuarquivo import checkMsgNroUnico
from typing import List, Tuple, Dict, Any, Union
import re
from functools import reduce
from dataclasses import dataclass
from ..utils import my_logger

log = my_logger.createLogger(__name__)


# --- Regular expressions precompiled for performance ---
_RE_NUM_UNICO = re.compile(r"(\d{6,})+")
_RE_DIVERGENCIA = re.compile(r"Divergência")
_RE_ARQUIVO = re.compile(r"Arquivo:\s*(\d+)")
_RE_LIVRO_FISCAL = re.compile(r"Livro\sFiscal")



@dataclass(frozen=True)
class Aviso():
    text: str


def update_nuarquivos() -> list[Dict[str, Any]]:
    """Atualiza lista de dicionarios contendo nuarquivo nunota e numnota.

    Returns:
        list[Dict[str, Any]]: _description_
    """

def fetch_nnn(num_notas) -> list[Dict[str, Any]]:
    """Cria dicionario com nuarquivo, nunota e numnotas de acordo com numnotas

    Returns:
        list[Dict[str, Any]]: _description_
    """
    n_str = ",".join(map(str,num_notas))

    queryResult = Query(
                        f"""select ixn.nuarquivo, ixn.nunota, ixn.numnota, cab.statusnota 
                        from tgfixn ixn
                        left join tgfcab cab on ixn.nunota = cab.nunota 
                        where ixn.numnota in ({n_str})"""
                    )
    for q in queryResult:
        nuar = q["NUNOTA"]
        q["NUNOTA"] = {
            "$": nuar or "",
            "chaves_rel": []
        }
    return queryResult

def fetch_nuarquivos(num: List[Dict[str, any]]) -> List[int]:
    """
    Retorna o nuarquivo caso não exista Nunota

    :return List[int | str]: Retorna uma lista de numeros inteiros 
    """
    r = []
    for nd in num:
        if nd["NUNOTA"]["$"] == "":
            r.append(nd["NUARQUIVO"])
    return r

def fetch_nunotas(num_dict: List[Dict[str, any]]) -> List[int]:
    return [ n["NUNOTA"]["$"]
        for n in num_dict
        if n["NUNOTA"]["$"] != ""
    ]

def fetch_config(nu_arquivo: int | str) -> Dict[str, Any]:
    return Query(
                        f"""select ixn.nuarquivo, ixn.config
                        from tgfixn ixn
                        where ixn.nuarquivo in ({nu_arquivo})"""
                    )

def validate_num_dict(num_dict: Dict[str, Any]) -> bool:
    for n in num_dict:
        if n["NUNOTA"]["$"] != "":
            return True
    return False


def processar_nuarquivos(pendentes: List[int | str]) -> List[Dict[str, any]]:
    """
    Processa Notas individualmente e extrai digergencias

    :return Dict: Divergecias em formato de dicionario
    """

    nro_unicos = []

    for p in pendentes:

        r = processarNotaArquivo([p])

        print(f"processarNotaArquivo {r}")

        nrou = extract_divergence(r)

        if nrou:
            nro_unicos.append(nrou)

    print(f"processar_nuarquivos nro_unicos: {nro_unicos}")

    return nro_unicos


def extract_divergence(r: Dict[str, Any]) -> int:
    """
    Retorna numero unico se caso exista dentro do aviso passado como argumento
    """
    if r.get('avisos'):
        if _RE_DIVERGENCIA.search(r['avisos']['aviso']["$"]):
            m = _RE_NUM_UNICO.search(r["statusMessage"])
            return m.group(0)
    elif r.get('aviso'):
        if _RE_DIVERGENCIA.search(r['aviso']['AVISO']["$"]):
            print(f"AVISO: {r['aviso']['AVISO']["$"]}")
            m = _RE_ARQUIVO.search(r['aviso']['AVISO']["$"])

            # Procura pela coluna config do nuarquivo m.group(1) e extrai numero da divergencia
            config = fetch_config(m.group(1))[0]["CONFIG"]
            msgConfig = checkMsgNroUnico(config)
            print(f"MSGCONFIG: {msgConfig}")
            nro_unico = _RE_NUM_UNICO.findall(msgConfig)
            return nro_unico

    else:
        if r.get("statusMessage"):
            if _RE_LIVRO_FISCAL.search(r["statusMessage"]):
                m = _RE_NUM_UNICO.search(r["statusMessage"])
                print(f"_RE_NUM_UNICO: {m.group(0)}")
                return m.group(0)
            else:
                log.warning("Não tem aviso de importação \n MSG: %s", r)
    return None

def resolve_divergences(div: Dict[str, Any]) -> None:
    for n in div:
        print()


def remover_fiscal(nros: List[str]) -> None:
    """
    Para cada número único, remove entradas do livro fiscal.
    """
    print(f"remove_fiscal: {nros}")
    def limpar(nro: str) -> None:
        registros = pesquisaPedidoLivroFiscal(nro)
        if registros:
            pks = [dict(NUNOTA=r[0], ORIGEM=r[1], SEQUENCIA=r[2], CODEMP=r[3]) for r in registros]
            removePedidoLivroFiscal(pks=pks)
        else:
            log.info("Número único %s não está no livro fiscal", nro)
    list(map(limpar, nros))  # map para side-effects

def mudar_frete(nros: List[str | int]) -> Dict[str, Any]:
    """
    Executa ação de frete para os números únicos.
    """
    param_str = ",".join(nros)
    print(f"nros unicos para mudar frete incluso: {param_str}")
    return actionButton(id=146, param=[{"type": "S", "paramName": "NUNOTA", "$": param_str}])

def pipeline(data: Any, steps: List[Callable[[Any], Any]]) -> Any:
    """
    Encadeia uma sequência de funções com reduce, interrompendo se o r for None ou vazio.
    """
    def apply_step(acc, fn):
        if acc is None:
            log.warning("Acc is None %s",acc)
        if isinstance(acc, (list, dict, str)) and not acc:
            log.warning("isinstance %s",acc)
        return fn(acc)

    return reduce(apply_step, steps, data)

def launch_cte(num_notas: List[int]):
    
    if not num_notas:
        print("Precisa de numero das notas!!")
        return None
        
    condition = True

    while condition:

        # Cria lista dicionario inicial dos numeros necessarios para importação
        NUM_DICT = fetch_nnn(num_notas)

        print(json.dumps(NUM_DICT, indent=4))

        nu_arquivos = fetch_nuarquivos(NUM_DICT)

        if not nu_arquivos:
            NUNOTA = fetch_nunotas(NUM_DICT)
            print(f"NUNOTAS: {NUNOTA}")

        else:
            #Processa Notas individualmente e retorna numero unico das divergencias
            nro_unico_divergencia = processar_nuarquivos(nu_arquivos)
            if nro_unico_divergencia:
                for n in nro_unico_divergencia:
                        remover_fiscal(n)
                        muda_frete = mudar_frete(n)
            
                print(f"resultado muda_frete: {muda_frete}")

        NUM_DICT = fetch_nnn(num_notas)
        condition = validate_num_dict(num_dict=NUM_DICT)


    # Processa nuarquivos que ainda não tem nota

    # Pega divergencias dos processados

    # Remove Livro Fiscal se houver

    # Muda Frete Incluso

    # Valida importação

    # confirma nota


launch_cte([
6403194,
6403209,
6403228,
6403248,
6403265,
6403447,
6406283,
6406581,
6406586,
6406594,
6406688,
6406689,
6406691,
6406693,
6406694,
6406696,
6406698,
6409110,
6409124,
6411128,
6413304,
6413332,
6413974,
6414356,
6415995,
6415997,
6416687,
6416722,
6416728,
6416735,
6417283,
6417832,
6418589,
6418587,
6418594,
6418597,
6418715,
6418732,
6420311,
6420633,
45372,
6423112,
6423139,
6423171,
6423187,
6423659,
6424134,
6424135,
6424136,
6424137,
6424138,
6426650,
6426724,
6426730,
6426748,
6426753,
6426967,
6427402,
6427410,
6427669,
6427706,
59260,
6429187,
6429214,
6429220,
6429232,
6429237,
6429241,
6429429,
165365,
6431046
])