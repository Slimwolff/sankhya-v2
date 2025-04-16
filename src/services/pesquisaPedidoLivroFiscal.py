from .carregarRegistros import carregarRegistros

def pesquisaPedidoLivroFiscal(nroUnico: str):

    """ 
        :param nroUnico: número unico do pedido que já está no livro fiscal de ICMS
        :return: Lista contendo os campos para apagar os registros
        :rtype: list[list]
    """
    r = carregarRegistros(
        entityName="MovimentoLivroFiscal",
        crudListener="br.com.sankhya.livrosfiscais.listeners.CadastroLivroFiscalCRUDListener",
        fields=[
            "NUNOTA",
            "ORIGEM",
            "SEQUENCIA",
            "CODEMP"
        ],
        expression=f"this.NUNOTA = ({nroUnico})",
        dataSetID="00I",
        ignoreListenerMethods="interceptEntitiesElement,interceptMetadataFields"
    )
    return r["result"]