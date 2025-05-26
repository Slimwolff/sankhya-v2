from typing import Dict, Any
from utils.wrapper import wrapper

def AlterarNota(keysToChange: Dict[str, Any]) -> Dict[str, Any]:
    """Altera o pedido do nro_unico

    Args:
        nroUnico (int | str): _description_
        keysToChange Dict[str, Any]: {key: value} com coluna e valor que quer mudar

    Returns:
        Dict[str, Any]: _description_
    """

    changies = keysToChange


    print(changies)

    r = wrapper.request(
        "CACSP.incluirAlterarCabecalhoNota", requestBody={
            "nota": {
                "ownerServiceCall": "CentralNotas_CentralNotas_4",
                "showClientEventAlteracaoValorVendaMais": "True",
                "txProperties": {
                "prop": [
                    {
                    "name": "br.com.sankhya.mgefin.checarfinanceiro.VlrEntrada",
                    "value": 0
                    },
                    {
                    "name": "br.com.sankhya.mgefin.recalculo.custopreco.Automatico",
                    "value": True
                    },
                    {
                    "name": "cabecalhoNota.inserindo.pedidoWeb",
                    "value": False
                    },
                    {
                    "name": "br.com.sankhya.mgefin.checarfinanceiro.RecalcularVencimento",
                    "value": False
                    }
                ]
                },
                "cabecalho": changies
            },
            "clientEventList": {
                "clientEvent": [
                {
                    "$": "br.com.sankhya.comercial.recalcula.pis.cofins"
                },
                {
                    "$": "br.com.sankhya.actionbutton.clientconfirm"
                },
                {
                    "$": "br.com.sankhya.recebimento.com.cartao.antes.aprovacao.sefaz"
                },
                {
                    "$": "br.com.sankhya.aprovar.nota.apos.recebimento.cartao"
                },
                {
                    "$": "br.com.sankhya.aprovar.nota.apos.baixa"
                },
                {
                    "$": "br.com.sankhya.exibir.variacao.valor.item"
                },
                {
                    "$": "br.com.sankhya.mgecom.compra.SolicitacaoComprador"
                },
                {
                    "$": "br.com.sankhya.mgecom.valida.ChaveNFeCompraTerceiros"
                },
                {
                    "$": "br.com.sankhya.mgecom.expedicao.SolicitarUsuarioConferente"
                },
                {
                    "$": "br.com.sankhya.mgecom.nota.adicional.SolicitarUsuarioGerente"
                },
                {
                    "$": "br.com.sankhya.mgecomercial.event.cadastrarDistancia"
                },
                {
                    "$": "br.com.sankhya.mgecomercial.event.baixaPortal"
                },
                {
                    "$": "br.com.sankhya.mgecomercial.event.faturamento.confirmacao"
                },
                {
                    "$": "br.com.sankhya.mgecomercial.event.compensacao.credito.debito"
                },
                {
                    "$": "br.com.utiliza.dtneg.servidor"
                },
                {
                    "$": "br.com.sankhya.mgefin.solicitacao.liberacao.orcamento"
                },
                {
                    "$": "br.com.sankhya.exibe.msg.variacao.preco"
                },
                {
                    "$": "br.com.sankhya.importacaoxml.cfi.para.produto"
                },
                {
                    "$": "br.com.sankhya.mgecom.parcelas.financeiro"
                },
                {
                    "$": "br.com.sankhya.mgecom.cancelamento.notas.remessa"
                },
                {
                    "$": "br.com.sankhya.comercial.solicitaContingencia"
                },
                {
                    "$": "br.com.sankhya.modelcore.comercial.centrais.alteracao.pedido.venda.mais"
                },
                {
                    "$": "br.com.sankhya.modelcore.comercial.centrais.alteracao.pedido.venda.mais.sem.limite"
                },
                {
                    "$": "central.save.grade.itens.mostrar.popup.serie"
                },
                {
                    "$": "central.save.grade.itens.mostrar.popup.info.lote"
                },
                {
                    "$": "br.com.sankhya.mgecom.central.itens.VendaCasada"
                },
                {
                    "$": "br.com.sankhya.exclusao.gradeProduto"
                },
                {
                    "$": "br.com.sankhya.mgecomercial.event.estoque.componentes"
                },
                {
                    "$": "br.com.sankhya.mgecomercial.event.estoque.insuficiente.produto"
                },
                {
                    "$": "br.com.sankhya.mgecom.central.itens.KitRevenda"
                },
                {
                    "$": "br.com.sankhya.mgecom.central.itens.KitRevenda.msgValidaFormula"
                },
                {
                    "$": "br.com.sankhya.mgecom.imobilizado"
                },
                {
                    "$": "br.com.sankhya.mgecom.item.multiplos.componentes.servico"
                },
                {
                    "$": "br.com.sankhya.mgecom.coleta.entrega.recalculado"
                },
                {
                    "$": "br.com.sankhya.central.alteracao.moeda.cabecalho"
                },
                {
                    "$": "br.com.sankhya.mgecom.event.troca.item.por.produto.substituto"
                },
                {
                    "$": "br.com.sankhya.mgecom.event.troca.item.por.produto.alternativo"
                },
                {
                    "$": "br.com.sankhya.modelcore.comercial.centrais.alteracao.pedido.venda.mais.item"
                },
                {
                    "$": "br.com.sankhya.modelcore.comercial.centrais.alteracao.pedido.venda.mais.item.sem.limite"
                },
                {
                    "$": "br.com.sankhya.mgeprod.producao.terceiro.inclusao.item.nota"
                }
                ]
            }
        },
    cookie="mgecom"
    )
    return r