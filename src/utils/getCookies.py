import browsercookie

class Cookies():
    def __init__(self, browser: str):
        self.sankhya_cookies = {
            "mge": {
                "JSESSIONID": ""
            },
            "mgefin": {
                "JSESSIONID": ""
            }, 
            "mgecom": {
                "JSESSIONID": ""
            }, 
            "mgecom-bff": {
                "JSESSIONID": ""
            }
        }
        browser_cookie = {
                "chrome": browsercookie.chrome,
                "firefox": browsercookie.firefox,
                "brave": browsercookie.brave
            }
        cookiejar = browser_cookie.get(browser, lambda: ValueError(f"Unsupported browser: {browser}"))()

        for __i in cookiejar:
            if __i.name == "JSESSIONID":
                valor = __i.value

                if self.sankhya_cookies.get(__i.path.strip("/")) == {"JSESSIONID": ""}:
                    self.sankhya_cookies[__i.path.strip("/")]["JSESSIONID"] = valor
    
    def get(self):
        return self.sankhya_cookies
