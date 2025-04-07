# Processar arquivos em lotes
# Pega NUARQUIVO
# Pega Divergencias ligadas ao NUARQUIVO
# Executa Botão de ação com numero unico das divergencias
# valida importação de cada NUARQUIVO
# troca parceiro caso necessario
# confirma nota
# renegoceia titulo com numero do documento informado
import json
from ..services.carregarRegistros import carregarRegistros

def getNuarquivoFromNumnotas(*nu):
    n = ",".join(str(element) for element in nu)
    print(n)
    records = carregarRegistros(entityName="ImportacaoXMLNotas",
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
    arr = records['responseBody']['result']
    nuArquivo = []
    for n in arr:
        nuArquivo.append(n[0])
    return nuArquivo
    

getNuarquivoFromNumnotas(6357523,6366813)