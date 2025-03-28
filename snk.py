import json
import browsercookie
import requests
from typing import Any
from enum import Enum

cookiejar = browsercookie.brave()
sankhya_cookies = {"mge": "", "mgefin": "", "mgecom": "", "mgecom-bff": ""}
for __i in cookiejar:
    if __i.name == "JSESSIONID":
        valor = __i.value
        if sankhya_cookies.get(__i.path.strip("/")) == "":
            sankhya_cookies[__i.path.strip("/")] = valor

print(sankhya_cookies)

mge = {"JSESSIONID": sankhya_cookies["mge"]}
mgefin = {"JSESSIONID": sankhya_cookies["mgefin"]}
mgecom = {"JSESSIONID": sankhya_cookies["mgecom"]}

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=UTF-8",
}

def snkRequest(
        URL: str,
        servico: str,
        corpo_requisicao: dict[str, Any],
        cookie="mge",
        parametros_adicionais={},
    ):
        data = {"serviceName": servico, "requestBody": corpo_requisicao}
        params = {
            "serviceName": servico,
            "outputType": "json",
        }
        params.update(parametros_adicionais)
        assert cookie in ("mge", "mgefin", "mgecom")
        if cookie == "mge":
            r = requests.post(
                URL,
                params=params,
                cookies=mge,
                headers=HEADERS,
                json=data,
            )
        elif cookie == "mgefin":
            r = requests.post(
                URL,
                params=params,
                cookies=mgefin,
                headers=HEADERS,
                json=data,
            )
        elif cookie == "mgecom":
            r = requests.post(
                URL,
                params=params,
                cookies=mgecom,
                headers=HEADERS,
                json=data,
            )

        return r


class Erro(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

serviceName = "DatasetSP.loadRecords"
corpo = {
        "dataSetID": "001",
        "entityName": "ImportacaoXMLNotas",
        "standAlone": False,
        "orderByExpression": "NUARQUIVO",
        "fields": [
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
            "VLRNOTA",
            "DHEMISS",
            "TIPO",
            "DHPROCESS",
            "DHIMPORT",
            "NUMNOTA",
            "CHAVEACESSO",
            "DETALHESIMPORTACAO",
            "STATUS",
            "NUNOTA",
            "NUFIN",
            "TIPIMPCTE",
            "DTVENC"
      ],
    #   "tryJoinedFields": False,
    #   "parallelLoader": True,
      "crudListener": "br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
      "criteria": {
        "expression": "(onlydate(this.DHEMISS) >= '01/03/2025') AND ((ImportacaoXMLNotas.NUMNOTA IN (251871,251876,252126)))",
        "parameters": [
        #   {
        #     "type": "S",
        #     "value": "01/03/2025"
        #   }
        ]
      }

}

r = snkRequest(URL="https://soldasul.sankhyacloud.com.br/mge/service.sbr",corpo_requisicao=corpo,servico=serviceName)

try:
    data = json.dumps(r.json(), indent=4)
    print(data)
except json.JSONDecodeError:
    raise Erro(r.text)