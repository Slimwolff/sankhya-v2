from typing import Any
from utils.wrapper import wrapper

def deletarRegistros(
        entityName: str,
        crudListener: str,
        pks: list,
        dataSetID="00I",
        **kwargs,
        
    ) -> dict | Any:
    reqBody = {
        "dataSetID": dataSetID,
        "entityName": entityName,
        "standAlone": False,
        "pks": pks,
        "crudListener": crudListener,
    }
    reqBody.update(kwargs)
    service = "DatasetSP.removeRecord"
    return wrapper.request(serviceName=service, requestBody=reqBody)