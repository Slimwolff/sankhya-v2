from typing import Dict, Any
from utils.wrapper import wrapper

def Query(sqlExpression: str) -> Dict[str, Any]:
    """Retorna os metadados das colunas e as resposta de cada linha em uma lista.

    Args:
        sqlExpression (str): SQL expression with select or with on init

    Returns:
        List[Dict[str, Any]]: Lista com dicionario de cada linha contendo coluna e valor.
    """
    r= wrapper.request(
        "DbExplorerSP.executeQuery",
        requestBody={
            "sql": sqlExpression
        }
    
    )
    fields_metadata = r["fieldsMetadata"]
    # aqui estão os resultados de fato
    rows = r["rows"]

    result = []
    for row in rows:
        dict_version = {}
        for index in range(len(row)):
            dict_version[fields_metadata[index]["name"]] = row[index]
        result.append(dict_version)

    print(f"query result: {result}")

    return result
