import json
import requests
from typing import Any
from pathlib import Path
from .getCookies import Cookies



class Snk():
    def __init__(
            self, 
            url:str, 
            browser: str,
        ):
        self.URL = url
        try:
            c = Cookies(browser).getLocalNetCookies("localhost","80") 
            if c.get("mge") is not None:
                self.cookies = c
            else:
                self.cookies = Cookies(browser).get()
                
        except Exception as e:
            print(e)
            self.cookies = Cookies(browser).get()
        

        print(f"Cookies used in request: {self.cookies}")
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

        assert cookie in ("mge", "mgefin", "mgecom")
        if cookie == "mge":
            r = requests.post(
                self.URL+f"/{"mge"}/service.sbr",
                params=params,
                cookies=self.cookies["mge"],
                headers=self.headers,
                json=data,
            )
        elif cookie == "mgefin":
            r = requests.post(
                self.URL+f"/{"mgefin"}/service.sbr",
                params=self.params,
                cookies=self.cookies["mgefin"],
                headers=self.headers,
                json=data,
            )
            
        elif cookie == "mgecom":
            r = requests.post(
                self.URL+f"/{"mgecom"}/service.sbr",
                params=self.params,
                cookies=self.cookies["mgecom"],
                headers=self.headers,
                json=data,
            )
        try:
            data = self.response(r.json())
            return data
        except json.JSONDecodeError:
            print(Error(r.text))

    def response(self,res: dict):
        if "responseBody" in res:
            return res['responseBody']

        raise Exception(f"responseBody não encontrado \n STATUS: {res['status']} \n MESSAGE: {res['statusMessage']}")
    


class Error(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message
