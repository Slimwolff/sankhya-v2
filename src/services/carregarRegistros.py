from typing import Any
from ..utils.wrapper import wrapper

def carregarRegistros(
        entityName: str,
        crudListener: str,
        orderByExpression: str,
        fields: list,
        expression: str,
        parameters = []
    ) -> dict | Any:
    reqBody = {
        "dataSetID": "001",
        "entityName": entityName,
        "standAlone": False,
        "orderByExpression": orderByExpression,
        "fields": fields,
        "tryJoinedFields": True,
        "parallelLoader": True,
        "crudListener": crudListener,
        "criteria": {
            "expression": expression,
            "parameters": parameters
        }
    }
    service = "DatasetSP.loadRecords"
    return wrapper.request(serviceName=service, requestBody=reqBody)