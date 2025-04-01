from utils import Snk

class Wrapper():
    def __init__(self):
        self.wrapper = Snk(

        )

    def init(self):
        pass


    headers 
    
    params = {
            "serviceName": serviceName,
            "outputType": "json",
        }

def load_config() -> dict:
    try:     
        # Load config file
        config_path = Path(__file__).resolve().parent.parent.parent / "config" / "config.toml"
        with open(config_path, "rb") as f:
            return tomllib.load(f)['env']
    except Error as e:
        print(f"erro na configuração: {e}")