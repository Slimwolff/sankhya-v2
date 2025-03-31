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
            "outputType": "json"
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

serviceName = "ActionButtonsSP.executeScript"
def corpo(param: str):
    return  {
            "runScript": {
                "actionID": 146,
                "masterEntityName": "CabecalhoNota",
                "params": {
                    "param": [
                        {
                            "type": "S",
                            "paramName": "NUNOTA",
                            "$": param
                        }
                    ]
                }
            }
        }
    

print(corpo('158156'))

r = snkRequest(
    URL="https://soldasul.sankhyacloud.com.br/mge/service.sbr",
    corpo_requisicao=corpo('158156'),
    servico=serviceName
)

try:
    data = json.dumps(r.json(), indent=4)
    print(data)
except json.JSONDecodeError:
    raise Erro(r.text)