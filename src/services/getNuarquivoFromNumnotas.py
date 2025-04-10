from services.carregarRegistros import carregarRegistros


def getNuarquivoFromNumnotas(date: str, nu: list):

    n = ",".join(str(element) for element in nu)

    print(f"numnotas: {n}")

    records = carregarRegistros(
        entityName="ImportacaoXMLNotas",
        crudListener="br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
        orderByExpression="NUARQUIVO",
        fields=[
            "NUARQUIVO",
            "DIASEMISSAOCALC",
            "TipoOperacao.DESCROPER",
            "CODEMP",
            "Empresa.NOMEFANTASIA",
            "CODPARC",
            "Parceiro.NOMEPARC",
            "CODVEND",
            "SITUACAOMDE",
            "IMPORTADOMDE",
            "SITUACAONFE",
            "TEMXML",
            "VLRNOTA",
            "DHEMISS",
            "TIPO",
            # "CONFIG",
            "DHPROCESS",
            # "XML",
            "DHIMPORT",
            "NUMNOTA",
            # "NUARQUIVO",
            "CHAVEACESSO",
            "DETALHESIMPORTACAO",
            "NOMEARQUIVO",
            "STATUS",
            "NUNOTA",
            "NUFIN",
            "TIPIMPCTE",
        ],
        expression=f"(onlydate(this.DHEMISS) >= {'01/03/2025'}) AND ((ImportacaoXMLNotas.NUMNOTA IN ({n}) ))"
    )
    print(f"getNuArquivoFromNumnotas -> records{records}")
    arr = records['responseBody']['result']
    nuArquivo = []
    for n in arr:
        nuArquivo.append(n[0])
    return nuArquivo