import re
from .carregarRegistros import carregarRegistros

def fixCte(nuarquivo: list):

    n = ",".join(str(element) for element in nuarquivo)
    print(n)
    resp = carregarRegistros(
        entityName="ImportacaoXMLNotas",
        crudListener="br.com.sankhya.modelcore.comercial.ImportacaoXmlNotasCrudListener",
        orderByExpression="NUARQUIVO",
        fields=[
            "NUARQUIVO",
            "CONFIG"
        ],
        expression=f"(onlydate(this.DHEMISS) >= {'01/03/2025'}) AND ((ImportacaoXMLNotas.NUARQUIVO IN ({n}) ))"
    )

    print(resp)


fixCte([12574, 12580])