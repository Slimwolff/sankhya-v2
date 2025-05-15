from typing import Dict, Any
from utils.wrapper import wrapper

def confirmarNota(nroUnico: int | str) -> Dict[str, Any]:
    """Retorna respota da confirmação da Nota

    Args:
        nroUnico (int | str): _description_

    Returns:
        Dict[str, Any]: _description_
    """
    r = wrapper.request("CACSP.confirmarNota",requestBody={
        "nota": {
            "confirmacaoCentralNota": "true",
            "ehPedidoWeb": "false",
            "atualizaPrecoItemPedCompra": "false",
            "ownerServiceCall": "CentralNotas_CentralNotas_0",
            "visAutOcorrencias": "true",
            "NUNOTA": {
                "$": nroUnico
            }
        }
    },
    cookie="mgecom"
    )
    print(r)
    return r