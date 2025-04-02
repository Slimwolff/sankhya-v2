import snk_request as snk from utils
#from utils import Cookies

snk = Snk(
    "https://soldasul.sankhyacloud.com.br",
    "brave"
)

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
    service = "DatasetSP.loadRecordss"
    r = snk.request(
        serviceName=service,
        requestBody=reqBody,
    )

    return r.json()

notas = carregarRegistros(
    entityName="ImportacaoXMLNotas",
    crudListener="br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
    orderByExpression="NUARQUIVO",
    fields=[
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
        "CONFIG",
        "DHPROCESS",
        "XML",
        "DHIMPORT",
        "NUMNOTA",
        "NUARQUIVO",
        "CHAVEACESSO",
        "DETALHESIMPORTACAO",
        "NOMEARQUIVO",
        "STATUS",
        "NUNOTA",
        "NUFIN",
        "TIPIMPCTE",
    ],
    expression=f"(onlydate(this.DHEMISS) >= {'01/03/2025'}) AND ((ImportacaoXMLNotas.NUMNOTA IN ({'608554,609582,610715'})))"
)

print(notas)