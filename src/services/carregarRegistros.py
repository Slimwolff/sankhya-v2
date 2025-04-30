from typing import Any
from utils.wrapper import wrapper

def carregarRegistros(
        entityName: str,
        crudListener: str,
        fields: list,
        expression: str,
        parameters = [],
        dataSetID="001",
        **kwargs
    ) -> dict | Any:
    reqBody = {
        "dataSetID": dataSetID,
        "entityName": entityName,
        "standAlone": False,
        "fields": fields,
        "tryJoinedFields": True,
        "parallelLoader": True,
        "crudListener": crudListener,
        "criteria": {
            "expression": expression,
            "parameters": parameters
        }
    }
    reqBody.update(kwargs)
    service = "DatasetSP.loadRecords"
    return wrapper.request(serviceName=service, requestBody=reqBody)