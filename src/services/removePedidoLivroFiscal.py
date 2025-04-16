from .deletarRegistros import deletarRegistros

def removePedidoLivroFiscal(pks: list):
    r = deletarRegistros(
        entityName="MovimentoLivroFiscal",
        crudListener="br.com.sankhya.livrosfiscais.listeners.CadastroLivroFiscalCRUDListener",
        pks=pks,
        ignoreListenerMethods="interceptEntitiesElement,interceptMetadataFields"
    )

    return r
