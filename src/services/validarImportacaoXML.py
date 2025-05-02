from utils.wrapper import wrapper

def validarImportacaoXML(nuArquivo: int, chavesReferenciadas: list) :

    requestBody = {
        "params": {
            "nuArquivo": nuArquivo,
            "codParceiro": {},
            "filtraSomentePedidos": False,
            "importarDadosDoInterm": False,
            "paramsCte": {
                "codTipOpCte": {
                "$": "1607"
                },
                "codBancoCte": {
                "$": "1"
                },
                "codNatCte": {
                "$": "2030000"
                },
                "codTipTitCte": {
                "$": "4"
                },
                "codCenterResultCte": {
                "$": "103003"
                },
                "tipoDataCte": {
                "$": "N"
                },
                "obtencaoCFOP": {
                "$": "T"
                },
                "importaCabCTe": {
                "$": "true"
                },
                "tipoImportacaoCabCte": {
                "$": "C"
                },
                "codTipOperCabCTe": {
                "$": "1414"
                },
                "codTipNegCabCTe": {
                "$": "483"
                },
                "codServCabCTe": {
                "$": "100006"
                },
                "tipoBuscaPedFrete": {
                "$": "C"
                },
                "codCenCusCabCTe": {
                "$": "F"
                },
                "codNatCabCTe": {
                "$": "F"
                },
                "codProjCabCTe": {
                "$": "F"
                },
                "copiaRateioPedFrete": {
                "$": "false"
                },
                "copiaCompradorPedFrete": {
                "$": "false"
                },
                "copiaCotacaoPedFrete": {
                "$": "false"
                },
                "copiaObsPedFrete": {
                "$": "false"
                },
                "copiaObsItemPedFrete": {
                "$": "false"
                },
                "exigeVinculoNota": {
                "$": "S"
                },
                "exigePedFrete": {
                "$": "false"
                },
                "vinculaNotaNaoEletronica": {
                "$": "false"
                },
                "criterioRateio": {
                "$": "V"
                },
                "exigeCteComplementado": {
                "$": "false"
                },
                "tolerancia": {
                "$": "0"
                },
                "vincularCTeComplOrigem": {
                "$": "false"
                },
                "importarCTeDocAnterior": {
                "$": "false"
                },
                "permiteSelectParceiroMesmoCnpjCte": {
                "$": "N"
                },
                "considerarParcDestParcEntrega": {
                "$": "false"
                },
                "consideraICMSXml": {
                "$": "true"
                }
            },
            "pedidoFreteLigado": {
                "nroPedidoFrete": "",
                "vlrPedidoFrete": ""
            },
            "paramsNFe": {
                "importarTransportadora": {
                "$": "S"
                },
                "atualizarCodAnvisa": {
                "$": "N"
                },
                "atualizarInfoCombustivel": {
                "$": "N"
                },
                "usarTributacaoSistema": {
                "$": "N"
                },
                "converterCSTParaCSTAnt": {
                "$": "N"
                },
                "desconsiderarValidacao": {
                "$": "N"
                },
                "nuNotaModeloProdutorRural": {},
                "usarComoDtFaturamento": {
                "$": "ES"
                },
                "permiteAlteracaoNotaNaCentral": {
                "$": "S"
                },
                "priorizaDescricaoVinculacaoProdutos": {
                "$": "N"
                },
                "apuraDivergenciaICMSST": {
                "$": "N"
                },
                "permiteSelectParceiroMesmoCnpj": {
                "$": "N"
                },
                "dtPrevEntr": {
                "$": "NOR"
                },
                "variacaoMaxQtd": {
                "$": "0"
                },
                "limiteDivergST": {
                "$": "0"
                },
                "centroDoResultado": {
                "$": "4"
                },
                "natureza": {
                "$": "4"
                },
                "projeto": {
                "$": "1"
                },
                "comprador": {
                "$": "4"
                },
                "tipoDeNegociacao": {
                "$": "4"
                },
                "numCotacao": {
                "$": "4"
                },
                "observacao": {
                "$": "5"
                },
                "observacaoItem": {
                "$": "N"
                },
                "validacaoDoFinanceiro": {
                "$": "N"
                },
                "copiaDeRateio": {
                "$": "N"
                },
                "topSimulacaoNotaCompra": {},
                "validaControleAd": {
                "$": "S"
                },
                "qtdDiasDtExtemporaneaCompra": {
                "$": "0"
                },
                "filtraSomentePedidos": {
                "$": "N"
                },
                "importarDadosDoInterm": {
                "$": "N"
                },
                "vinculoManualDevol": {
                "$": "N"
                },
                "realizarConvCSTdeIPI": {
                "$": "N"
                },
                "considerarValoresIPIDevolVenda": {},
                "considerarCFOPdeBonificacaoImportacaoXML": {},
                "gravaChaveRefInexistente": {},
                "atualizarCodEAN": {}
            },
            "paramsNFeEmissaoPropria": {
                "codTipOpVenda": {
                "$": "1800"
                },
                "codTipOpDevVenda": {},
                "codTipOpDevCompra": {},
                "codTipOpComplemento": {},
                "codTipOpAjuste": {},
                "codTipNeg": {
                "$": "11"
                },
                "codNat": {},
                "codCCus": {},
                "codProj": {},
                "codTipOpCompra": {
                "$": "1452"
                },
                "chkvalidaCadastroParceiroNaImportacaoXML": {
                "$": "N"
                },
                "chkImportarDadosDoInterm": {
                "$": "N"
                },
                "qtdDiasDtExtemporanea": {
                "$": "0"
                },
                "validacaoDoFinanceiroEmissaoPropria": {}
            },
            "validacoes": {
                "simulacaoFinanceiro": False,
                "produtosParceiro": {
                "ITEMALTERADO": False,
                "produtoParceiro": []
                },
                "pedidosLigados": {
                "item": [],
                "ligarAntigos": False,
                "revalidarPedidosLigados": False
                },
                "impostos": {
                "USOIMPOSTOS": "N"
                },
                "financeiro": {
                "USOFINANCEIRO": "N"
                },
                "chavesReferenciadas": {
                "chavesReferenciadas": chavesReferenciadas
                },
                "frete": {
                    "ACEITARDIVERGENCIAS": False
                }
            },
            "reprocessar": False
        }
    }
    serviceName="ImportacaoXMLNotasSP.validarImportacao"
    return wrapper.request(
        serviceName=serviceName,
        requestBody=requestBody
    )
    