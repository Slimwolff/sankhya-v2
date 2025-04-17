from .carregarRegistros import carregarRegistros


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
        expression=f"(onlydate(this.DHEMISS) >= {date}) AND ((ImportacaoXMLNotas.NUMNOTA IN ({n}) ))"
    )
    arr = records['result']
    nuArquivo = []
    for n in arr:
        nuArquivo.append(n[0])
    return nuArquivo