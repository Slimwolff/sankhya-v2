from .carregarRegistros import carregarRegistros


def get_nuarquivo_from_numnotas(nu: list) -> list:
    """
        retorna uma lista com uma lista com os campos **NUNOTA**, **NUARQUIVO**, **NUMNOTA**
    """

    n = ",".join(str(element) for element in nu)

    records = carregarRegistros(
        entityName="ImportacaoXMLNotas",
        crudListener="br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
        orderByExpression="NUARQUIVO",
        fields=[
            "NUNOTA",
            "NUARQUIVO",
            "NUMNOTA"
        ],
        expression=f"((ImportacaoXMLNotas.NUMNOTA IN ({n})))"
    )
    return records['result']