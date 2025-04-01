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
        self.URL = url+"/mge/service.sbr"
        self.cookies = cookie
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "Content-Type": "application/json; charset=UTF-8",
        }


    def request(self, ):

        assert self.cookies in ("mge", "mgefin", "mgecom")
        if self.cookie == "mge":
            r = requests.post(
                self.URL,
                params=params,
                cookies=self.cookies.mge,
                headers=self.headers,
                json=self.data,
            )
        elif self.cookie == "mgefin":
            r = requests.post(
                self.URL,
                params=self.params,
                cookies=self.cookies.mgefin,
                headers=self.headers,
                json=self.data,
            )
            
        elif self.cookie == "mgecom":
            r = requests.post(
                self.URL,
                params=self.params,
                cookies=self.cookies.mgecom,
                headers=self.headers,
                json=self.data,
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
