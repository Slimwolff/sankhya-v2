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

nunotas = [
    171105,
    171103,
    170076,
    171106,
    170084,
    170805,
    170806,
    170807,
    170808,
    171107,
    171104
]

for nu in nunotas:
    print(f"nunota: {nu}")
    confirmarNota(nu)