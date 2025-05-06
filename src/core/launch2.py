import json
from services import *
from typing import List, Tuple, Dict, Any, Union
import re
import logging
from functools import reduce
from dataclasses import dataclass



def update_nuarquivos() -> list[Dict[str, Any]]:
    """Atualiza lista de dicionarios contendo nuarquivo nunota e numnota.

    Returns:
        list[Dict[str, Any]]: _description_
    """

def fetch_nuarquivos(num_notas) -> list[Dict[str, Any]]:
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
        if not q["NUNOTA"]:
            q["has_nota"] = False
        else:
            q["has_nota"] = True

    return queryResult

def launch_cte(num_notas: List[int]):
    
    if not num_notas:
        print("Precisa de numero das notas!!")
        return None
        
    # Cria lista dicionario inicial dos numeros necessarios para importação
    NUARQUIVOS_DICT = fetch_nuarquivos(num_notas)

    print(json.dumps(NUARQUIVOS_DICT, indent=4))

    for nd in NUARQUIVOS_DICT:
        if not nd["has_nota"]:
            processarNotaArquivo([nd])
    # Processa nuarquivos que ainda não tem nota

    # Pega divergencias dos processados

    # Remove Livro Fiscal se houver

    # Muda Frete Incluso

    # Valida importação

    # confirma nota


launch_cte([
    2612289,
    2612293
])