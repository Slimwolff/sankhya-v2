from .carregarRegistros import carregarRegistros


def getConfigFromNuarquivo(nuarquivo: list) -> list:
    """Pega o CAMPO 'config' que contain validacoes
       e retorna em um dicionario.

    :param nuarquivo: lista de numeros com nuarquivos
    :returns: Uma lista com dicionario contendo nuarquivo e config { nuarquivo: str, config: str/xml }
    :rtype: list
    """
    n = ",".join(str(element) for element in nuarquivo)

    print(f"numnotas: {n}")

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