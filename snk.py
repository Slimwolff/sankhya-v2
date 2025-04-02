import json
import browsercookie
import requests
from typing import Any
from enum import Enum

cookiejar = browsercookie.brave()
sankhya_cookies = {"mge": "", "mgefin": "", "mgecom": "", "mgecom-bff": ""}
for __i in cookiejar:
    if __i.name == "JSESSIONID":
        valor = __i.value
        if sankhya_cookies.get(__i.path.strip("/")) == "":
            sankhya_cookies[__i.path.strip("/")] = valor

print(sankhya_cookies)

mge = {"JSESSIONID": sankhya_cookies["mge"]}
mgefin = {"JSESSIONID": sankhya_cookies["mgefin"]}
mgecom = {"JSESSIONID": sankhya_cookies["mgecom"]}

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=UTF-8",
}

def snkRequest(
        URL: str,
        servico: str,
        corpo_requisicao: dict[str, Any],
        cookie="mge",
        parametros_adicionais={},
    ):
        data = {"serviceName": servico, "requestBody": corpo_requisicao}
        params = {
            "serviceName": servico,
            "application": "CentralNotasStack",
            "outputType": "json",
            "resourceID": "br.com.sankhya.com.mov.CentralNotas"
        }
        params.update(parametros_adicionais)
        assert cookie in ("mge", "mgefin", "mgecom")
        if cookie == "mge":
            r = requests.post(
                URL,
                params=params,
                cookies=mge,
                headers=HEADERS,
                json=data,
            )
        elif cookie == "mgefin":
            r = requests.post(
                URL,
                params=params,
                cookies=mgefin,
                headers=HEADERS,
                json=data,
            )
        elif cookie == "mgecom":
            r = requests.post(
                URL,
                params=params,
                cookies=mgecom,
                headers=HEADERS,
                json=data,
            )

        return r


class Erro(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

serviceName = "CACSP.incluirAlterarCabecalhoNota"
def corpo(date: str, notas: str):
    return  {
        
        "nota": {
        "ownerServiceCall": "CentralNotas_CentralNotas_0",
        "txProperties": {
          "prop": [
            {
              "name": "br.com.sankhya.mgefin.checarfinanceiro.VlrEntrada",
              "value": 0
            },
            {
              "name": "br.com.sankhya.mgefin.recalculo.custopreco.Automatico",
              "value": False
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
        "cabecalho": {
          "NUNOTA": {
            "$": "159712"
          },
          "CODPARC": {
            "$": "2"
          },
          "Parceiro.NOMEPARC": {
           "$": "SC EXPRESSO SAO MIGUEL SA"
          }
        }
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
    
    }
    

r = snkRequest(
    URL="https://soldasul.sankhyacloud.com.br/mgecom/service.sbr",
    corpo_requisicao=corpo('01/03/2025','251871,251876,252126' ),
    servico=serviceName
)

try:
    result = r.json()
    data = json.dumps(result, indent=4)
    print(data)
except json.JSONDecodeError:
    raise Erro(r.text)