from services import *
from typing import List, Tuple, Dict, Any, Union
import re
import logging
from functools import reduce
from dataclasses import dataclass


logger = logging.getLogger(__name__)

# --- Regular expressions precompiled for performance ---
_RE_NUM_UNICO = re.compile(r"(\d{6,})+")
_RE_DIVERGENCIA = re.compile(r"Divergência")
_RE_ARQUIVO = re.compile(r"Arquivo:\s*(\d+)")

# --- Domain models for clarity and immutability ---
@dataclass(frozen=True)
class NuArquivo:
    has_nota: bool
    id: int

@dataclass(frozen=True)
class Aviso:
    texto: str

# --- Functional utilities ---
def pipeline(data: Any, steps: List[Any]) -> Any:
    """
    Encadeia uma sequência de funções onde a saída de uma é a entrada da próxima.
    """
    return reduce(lambda acc, fn: fn(acc), steps, data)


# --- Data acquisition (I/O) functions ---
def get_nu_arquivos(numeros_notas: Tuple[int, ...]) -> List[NuArquivo]:
    """
    Busca pares (has_nota, nu_arquivo) para cada nota.
    """
    
    raw = get_nuarquivo_from_numnotas(list(numeros_notas))  # externa, retorna List[Tuple[bool,int]]
    print(f"raw after get_nuarquiv...() -> {raw}")
    return [NuArquivo(has_nota=(nunota not in (None, '')), id=nuarquivo) for nunota, nuarquivo, _ in raw]

# --- Pure transformation functions ---
def filter_pending(nu_arquivos: List[NuArquivo]) -> List[int]:
    """Filtra IDs de arquivos que ainda não têm nota.

    Args:
        nu_arquivos (list): lista de de dicionarios com 

    Returns:
        List[int]: _description_
    """
    print(f"filtrar pendentes: {nu_arquivos}")
    return [na.id for na in nu_arquivos if not na.has_nota]

def processar_arquivos(pendentes: List[int]) -> List[Aviso]:
    """
    Processa arquivos e retorna lista de avisos.
    """
    print(f"processar arquivos pendentes: {pendentes}")
    resultado = processarNotaArquivo(pendentes)  # externa

    avisos_raw = []

    if resultado.get('avisos'):
        avisos_raw = resultado['avisos']['aviso']
    elif resultado.get('aviso'):
        avisos_raw = resultado['aviso']['AVISO']

    return [Aviso(item.get('$', '')) for item in (avisos_raw if isinstance(avisos_raw, list) else [avisos_raw])]

def extrair_ids_divergencia(avisos: List[Aviso]) -> List[int]:
    """
    Extrai IDs de arquivos com divergência.
    """
    print(f"avisos: {avisos}")
    return [int(m.group(1))
            for aviso in avisos
            if _RE_DIVERGENCIA.search(aviso.texto)
            for m in (_RE_ARQUIVO.search(aviso.texto),)
            if m]

def get_nro_unico(ids_div: List[int]) -> List[str]:
    """
    Obtém números únicos a partir de IDs de arquivos divergentes.
    """
    print(f"get_nro_unico: {ids_div}")
    configs = getConfigFromNuarquivo(ids_div)  # externa, retorna List[Tuple, str]
    
    return [
        match
        for _, m in configs
        for match in _RE_NUM_UNICO.findall(checkMsgNroUnico(m))
    ]


# --- Side-effect functions (I/O) ---
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
            logger.info("Número único %s não está no livro fiscal", nro)
    list(map(limpar, nros))  # map para side-effects

def mudar_frete(nros: List[str | int]) -> Dict[str, Any]:
    """
    Executa ação de frete para os números únicos.
    """
    param_str = ",".join(nros)
    print(f"nros unicos para mudar frete incluso: {param_str}")
    return actionButton(id=146, param=[{"type": "S", "paramName": "NUNOTA", "$": param_str}])

def preparar_importacao(num_notas: list) -> List[Tuple[int, str]]:
    """
    Prepara pares (nu_arquivo, chave_referenciada).
    """
    raw = get_nuarquivo_from_numnotas(num_notas)

    # pega nuarquivos dos que não tem nota ainda
    nuarqs = [ nuarquivo for nunota, nuarquivo, _ in raw if not nunota ]

    def mapper(na: NuArquivo) -> Tuple[int, str]:
        cfg = getConfigFromNuarquivo([na])[0][1]
        chave = checkChaveReferenciada(cfg)
        return na, chave
    
    return [(mapper(n)) for n in nuarqs]

def validar_importacoes(pares: List[Tuple[int, str]]) -> List[Dict[str, Any]]:
    """
    Valida cada importação XML e retorna resultados.
    """
    return [
        {"nu_arquivo": nu, "resultado": validarImportacaoXML(nu, chave)}
        for nu, chave in pares
    ]

# --- Orquestração ---
def launch_cte_functional(numeros_notas: List[int]) -> Dict[str, Any]:
    """
    Fluxo de lançamento de CTe em estilo funcional.
    Retorna um resumo com ação de frete e status de importação.
    """
    # Pipeline principal: coleta, filtra, processa, extrai e obtém números únicos
    nros_unicos = pipeline(
        tuple(numeros_notas),
        [get_nu_arquivos, filter_pending, processar_arquivos, extrair_ids_divergencia, get_nro_unico]
    )

    
    if nros_unicos:
        # Side-effects independentes:
        remover_fiscal(nros_unicos)
        frete_action = mudar_frete(nros_unicos)


    # Validação de importações:
    pares_importacao = preparar_importacao(numeros_notas)

    print(pares_importacao)

    resultados_import = validar_importacoes(pares_importacao)

    results = {
        "frete_action": frete_action,
        "import_results": resultados_import
    }
    print(results)
    return results

launch_cte_functional([
    2612289,
    2612293,
    2612148,
    2612239,
    2611145,
    2614156,
    2610979,
    2612068,
    2612370,
    2611972,
    558156
])