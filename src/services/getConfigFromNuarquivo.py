from typing import List
from .carregarRegistros import carregarRegistros


def getConfigFromNuarquivo(nuarquivo: List[int | str]) -> list:
    """Pega o CAMPO 'config' que contain validacoes
       e retorna em um dicionario.

    :param nuarquivo: lista de numeros com nuarquivos
    :returns: Uma lista com dicionario contendo nuarquivo e config { nuarquivo: str, config: str/xml }
    :rtype: list[dict]
    """
    if not nuarquivo:
        return []
    else:
        n = ",".join(str(element) for element in nuarquivo)

    print(f"GetConfigFromNuarquivo | list: {n}")

    records = carregarRegistros(
        entityName="ImportacaoXMLNotas",
        crudListener="br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
        orderByExpression="NUARQUIVO",
        fields=[
            "NUARQUIVO",
            "CONFIG",
        ],
        expression=f"(ImportacaoXMLNotas.NUARQUIVO IN ({n}) )"
    )
    return records['result']