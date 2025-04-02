import json
import requests
from typing import Any
from pathlib import Path
from .getCookies import Cookie



class Snk():
    def __init__(
            self, 
            url:str, 
            cookie: dict[str, Any],
        ):
        self.URL = url
        self.cookies = cookie
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "Content-Type": "application/json; charset=UTF-8",
        }


    def request(
            self, 
            serviceName: str, 
            requestBody: dict[str, Any],
            cookie="mge",
            add_params={}
        ):

        params = {
            "serviceName": serviceName,
            "outputType": "json",
        }

        params.update(add_params)

        data = {"serviceName": serviceName, "requestBody": requestBody}

        assert self.cookies in ("mge", "mgefin", "mgecom")
        if cookie == "mge":
            r = requests.post(
                self.URL+f"/{"mge"}/service.sbr",
                params=params,
                cookies=self.cookies.mge,
                headers=self.headers,
                json=data,
            )
        elif cookie == "mgefin":
            r = requests.post(
                self.URL+f"/{"mgefin"}/service.sbr",
                params=self.params,
                cookies=self.cookies.mgefin,
                headers=self.headers,
                json=data,
            )
            
        elif cookie == "mgecom":
            r = requests.post(
                self.URL+f"/{"mgecom"}/service.sbr",
                params=self.params,
                cookies=self.cookies.mgecom,
                headers=self.headers,
                json=data,
            )
        try:
            data = json.dumps(r.json(), indent=4)
            return data
        except json.JSONDecodeError:
            raise Error(r.text)


class Error(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message
