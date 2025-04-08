# Processar arquivos em lotes
# Pega NUARQUIVO
# Pega Divergencias ligadas ao NUARQUIVO
# Executa Botão de ação com numero unico das divergencias
# valida importação de cada NUARQUIVO
# troca parceiro caso necessario
# confirma nota
# renegoceia titulo com numero do documento informado
import json
import re
from ..services.carregarRegistros import carregarRegistros
from ..services.processarNotaArquivo import processarNotaArquivo

def getNuarquivoFromNumnotas(nu: list):

    n = ",".join(str(element) for element in nu)

    print(f"numnotas: {n}")

    records = carregarRegistros(
        entityName="ImportacaoXMLNotas",
        crudListener="br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
        orderByExpression="NUARQUIVO",
        fields=[
            "NUARQUIVO",
            "DIASEMISSAOCALC",
            "TipoOperacao.DESCROPER",
            "CODEMP",
            "Empresa.NOMEFANTASIA",
            "CODPARC",
            "Parceiro.NOMEPARC",
            "CODVEND",
            "SITUACAOMDE",
            "IMPORTADOMDE",
            "SITUACAONFE",
            "TEMXML",
            "VLRNOTA",
            "DHEMISS",
            "TIPO",
            # "CONFIG",
            "DHPROCESS",
            # "XML",
            "DHIMPORT",
            "NUMNOTA",
            # "NUARQUIVO",
            "CHAVEACESSO",
            "DETALHESIMPORTACAO",
            "NOMEARQUIVO",
            "STATUS",
            "NUNOTA",
            "NUFIN",
            "TIPIMPCTE",
        ],
        expression=f"(onlydate(this.DHEMISS) >= {'01/03/2025'}) AND ((ImportacaoXMLNotas.NUMNOTA IN ({n}) ))"
    )
    print(f"getNuArquivoFromNumnotas -> records{records}")
    arr = records['responseBody']['result']
    nuArquivo = []
    for n in arr:
        nuArquivo.append(n[0])
    return nuArquivo
    

# getNuarquivoFromNumnotas(6357523,6366813)

def launchCTE(numNotas: list):
    nuArquivos = getNuarquivoFromNumnotas(numNotas)

    holding = processarNotaArquivo(nuArquivos)

    processedNotes = holding['responseBody']['avisos']['aviso']

    diverNotes = []

    for n in processedNotes:
        if re.search("Divergência",n["$"]) is not None:
            match = re.search(r'Arquivo:\s*(\d+)',n["$"])
            if match:
                diverNotes.append(match.group(1))
    print(diverNotes)

launchCTE([6332819,6334510,6337246])