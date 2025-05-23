from utils.wrapper import wrapper

def actionButton(id: int, param: list[dict]):
    print( wrapper.request(
        serviceName="ActionButtonsSP.executeScript",
        requestBody={
            "runScript": {
                "actionID": id,
                "refreshType": "NONE",
                "params": {
                    "param": param
                }
            }
        }
    ))