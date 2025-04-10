from ..utils.wrapper import wrapper

def carregarRegistros(
        entityName: str,
        crudListener: str,
        orderByExpression: str,
        fields: list,
        expression: str,
        parameters = []
    ):
    reqBody = {
        "dataSetID": "001",
        "entityName": entityName,
        "standAlone": False,
        "orderByExpression": orderByExpression,
        "fields": fields,
        "tryJoinedFields": True,
        "parallelLoader": True,
        "crudListener": crudListener,
        "criteria": {
            "expression": expression,
            "parameters": parameters
        }
    }
    service = "DatasetSP.loadRecords"
    return wrapper.response(wrapper.request(serviceName=service, requestBody=reqBody))

    

# notas = carregarRegistros(
#     entityName="ImportacaoXMLNotas",
#     crudListener="br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
#     orderByExpression="NUARQUIVO",
#     fields=[
#         "NUARQUIVO",
#         "DIASEMISSAOCALC",
#         "TipoOperacao.DESCROPER",
#         "CODEMP",
#         "Empresa.NOMEFANTASIA",
#         "CODPARC",
#         "Parceiro.NOMEPARC",
#         "CODVEND",
#         "SITUACAOMDE",
#         "IMPORTADOMDE",
#         "SITUACAONFE",
#         "TEMXML",
#         "VLRNOTA",
#         "DHEMISS",
#         "TIPO",
#         # "CONFIG",
#         "DHPROCESS",
#         # "XML",
#         "DHIMPORT",
#         "NUMNOTA",
#         # "NUARQUIVO",
#         "CHAVEACESSO",
#         "DETALHESIMPORTACAO",
#         "NOMEARQUIVO",
#         "STATUS",
#         "NUNOTA",
#         "NUFIN",
#         "TIPIMPCTE",
#     ],
#     expression=f"(onlydate(this.DHEMISS) >= {'01/03/2025'}) AND ((ImportacaoXMLNotas.NUMNOTA IN ({'608554,609582,610715'})))"
# )

# print(notas)