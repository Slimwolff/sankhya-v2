from typing import Any, Callable, List
import json
from ..services import *

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
                        f"""select ixn.nuarquivo, ixn.nunota, ixn.numnota, ixn.status, cab.statusnota 
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

def fetch_config(nu_arquivo: int | str) -> List[Dict[str, Any]]:
    return Query(
                        f"""select ixn.nuarquivo, ixn.config
                        from tgfixn ixn
                        where ixn.nuarquivo in ({nu_arquivo})"""
                    )

def validate_num_dict(num_dict: Dict[str, Any]) -> bool:
    for n in num_dict:
        if n["NUNOTA"]["$"] != "":
            return False
    return True


def processar_nuarquivos(pendentes: List[int | str]) -> List[int | str]:
    """
    Processa Notas individualmente e extrai digergencias

    :return List: Nro Unicos das divergecias em uma lista
    """

    nro_unicos = []

    for p in pendentes:

        # Processa nota individualmente e retorna resposta do processamento
        r = processarNotaArquivo([p])

        print(f"processarNotaArquivo {r}")

        #extrai divergencias em uma lista
        nro_unico_extracted = extract_divergence(r)

        #adiciona nro_unico das divergencias para uma lista
        if nro_unico_extracted:
            nro_unicos.extend(nro_unico_extracted)

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
                return [m.group(0)]
            else:
                log.warning("Não tem aviso de importação \n MSG: %s", r)
    return None

def resolve_divergences(div: Dict[str, Any]) -> None:
    for n in div:
        print(n)


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

def preparar_importacao(nu_arquivo: list) -> List[Tuple[int, str]]:
    """
    Prepara pares (nu_arquivo, chave_referenciada).
    """

    print(f"PREPARAR IMPORTAÇÃO: {nu_arquivo}")

    def mapper(nu: int | str) -> Tuple[int, str]:
        print(f"running Nu_arquivo: {nu}")
        cfg = fetch_config(nu)[0]["CONFIG"]
        chave = checkChaveReferenciada(cfg)
        return nu, chave
    
    return [(mapper(n)) for n in nu_arquivo]

def validar_importacoes(pares: List[Tuple[int, str]]) -> List[Dict[str, Any]]:
    """
    Valida cada importação XML e retorna resultados.
    """
    return [
        {"nu_arquivo": nu, "resultado": validarImportacaoXML(nu, chave)}
        for nu, chave in pares
    ]

def launch_cte(num_notas: List[int]):
    
    if not num_notas:
        print("Precisa de numero das notas!!")
        return None
        
    condition = True

    while condition:

        # Cria lista dicionario inicial dos numeros necessarios para importação
        NUM_DICT = fetch_nnn(num_notas)

        print(json.dumps(NUM_DICT, indent=4))

        # Retorna NU_ARQUIVOS que não tem NUNOTA
        nu_arquivos = fetch_nuarquivos(NUM_DICT)

        if not nu_arquivos:
            NUNOTA = fetch_nunotas(NUM_DICT)
            print(f"NUNOTAS: {NUNOTA}")
            condition = False

        else:

            # STATUS 0 = não processada
            # STATUS 4 = com divergencia
            # STATUS 2 = inserida com sucesso
            #
            
            # #Processa Notas individualmente e retorna divergencias
            nro_unico_divergencia = processar_nuarquivos(nu_arquivos)
            print(f"nro_unico_divergencia: {nro_unico_divergencia}")
            if nro_unico_divergencia:

                print(f"nro_unico_divergencia: {nro_unico_divergencia}")

                remover_fiscal(nro_unico_divergencia)
                muda_frete = mudar_frete(nro_unico_divergencia)

                print(f"resultado muda_frete: {muda_frete}")

                preparacao = preparar_importacao(nu_arquivo=nu_arquivos)

                print(f"RESULTADO PREPARAR IMPORTAÇÃO: {preparacao}")

                import_validation = validar_importacoes(preparacao)

                print(f"RESULTADO VALIDAR IMPORTACOES: {import_validation}")
            
        NUM_DICT = fetch_nnn(num_notas)
        condition = validate_num_dict(num_dict=NUM_DICT)


    print(NUM_DICT)

    # Processa nuarquivos que ainda não tem nota

    # Pega divergencias dos processados

    # Remove Livro Fiscal se houver

    # Muda Frete Incluso

    # Valida importação

    # confirma nota


launch_cte([
    6439177,
    6439209,
    6442265
])