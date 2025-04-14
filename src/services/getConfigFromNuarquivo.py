from .carregarRegistros import carregarRegistros


def getConfigFromNuarquivo(nu: list):

    n = ",".join(str(element) for element in nu)

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
    # print(f"getNuArquivoFromNumnotas -> records{records}")
    return records['result']