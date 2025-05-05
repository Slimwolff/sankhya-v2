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

    queryResult = Query(f"select nuarquivo, nunota, numnota from tgfixn where numnota in ({n_str})")

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
        
    # Cria dicionario inicial dos numeros necessarios para importação
    NUARQUIVOS_DICT = fetch_nuarquivos(num_notas)

    print(NUARQUIVOS_DICT)


launch_cte([
    2612289,
    2612293
])