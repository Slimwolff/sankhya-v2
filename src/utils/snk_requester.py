import requests
from typing import Any
import tomllib
import tomllib
from pathlib import Path
from .getCookies import Cookie

class Snk():
    def __init__(
            self, 
            url:str, 
            serviceName: str,
            requestBody: dict[str, Any],
            cookie="mge", 
            add_parameters = {}
        ):

        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "Content-Type": "application/json; charset=UTF-8",
        }

        self.params = {
            "serviceName": serviceName,
            "outputType": "json",
        }

        self.params.update(add_parameters)

        self.getCookie = Cookie("brave").get()
        self.cookie = self.getCookie[cookie]

        self.serviceName = serviceName
        self.data = { "serviceName": serviceName, "requestBody": requestBody }

        try:
            # Load config file
            config_path = Path(__file__).resolve().parent.parent.parent / "config" / "config.toml"
            with open(config_path, "rb") as f:
                data = tomllib.load(f)
        except:
                print("erro na configuração, confira o arquivo config.toml")
        
        self.URL = data.env.dominio


    def request(self,URL):
        URL = self.URL+f"/mge/service.sbr"
        
        assert self.cookie in ("mge", "mgefin", "mgecom")
        
        if self.cookie == "mge":
            r = requests.post(
                URL,
                params=self.params,
                cookies=self.mge,
                headers=self.HEADERS,
                json=self.data,
            )
        elif self.cookie == "mgefin":
            r = requests.post(
                URL,
                params=self.params,
                cookies=self.mge,
                headers=self.HEADERS,
                json=self.data,
            )
            
        elif self.cookie == "mgecom":
            r = requests.post(
                URL,
                params=self.params,
                cookies=self.mge,
                headers=self.HEADERS,
                json=self.data,
            )

        return r

