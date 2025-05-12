from typing import Any, Callable, List
import json
from services import *
from typing import List, Tuple, Dict, Any, Union
import re
from functools import reduce
from dataclasses import dataclass
from utils import my_logger

log = my_logger.createLogger(__name__)


# --- Regular expressions precompiled for performance ---
_RE_NUM_UNICO = re.compile(r"(\d{6,})+")
_RE_DIVERGENCIA = re.compile(r"Divergência")
_RE_ARQUIVO = re.compile(r"Arquivo:\s*(\d+)")


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
    r = []
    for nd in num:
        if nd["NUNOTA"]["$"] == "":
            r.append(nd["NUARQUIVO"])
    return r

def processar_nuarquivos(pendentes: List[int | str]) -> List[Dict[str, any]]:

    r = processarNotaArquivo(pendentes)

    avisos_raw = []

    if r.get('avisos'):
        avisos_raw = r['avisos']['aviso']
    elif r.get('aviso'):
        avisos_raw = r['aviso']['AVISO']

    return [Aviso(item.get('$', '')) for item in (avisos_raw if isinstance(avisos_raw, list) else [avisos_raw])]



def extract_divergence(avisos: List[Aviso]) -> List[int]:
    """
    Extrai IDs de arquivos com divergência.
    """
    print(f"avisos: {avisos}")
    return [int(m.group(1))
            for aviso in avisos
            if _RE_DIVERGENCIA.search(aviso.texto)
            for m in (_RE_ARQUIVO.search(aviso.texto),)
            if m]



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
        
    # Cria lista dicionario inicial dos numeros necessarios para importação
    NUM_DICT = fetch_nnn(num_notas)

    print(json.dumps(NUM_DICT, indent=4))

    nuars = fetch_nuarquivos(NUM_DICT)

    if not nuars:
        log.warning("not nuarquivos to process")
    else:
        processarNotaArquivo(nuars)



    # Processa nuarquivos que ainda não tem nota

    # Pega divergencias dos processados

    # Remove Livro Fiscal se houver

    # Muda Frete Incluso

    # Valida importação

    # confirma nota


launch_cte([
    558341
])