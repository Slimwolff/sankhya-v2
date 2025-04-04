from .load_config import getConfig
from .snk_requester import Snk
config = getConfig()
wrapper = Snk(
    f"http://{config['env']['dominio']}",
    config['env']['browser']
)