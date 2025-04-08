from ..utils.wrapper import wrapper

def processarNotaArquivo(nuArquivo: list):
    
    nid = []
    for n in nuArquivo:
        nid.append({"$":n})

    requestBody = {
        "params": {
            "multiplosAvisos": "true",
            "NUARQUIVO": nid,
            "paramsCte": {
                "codBancoCte": {
                    "$": "1"
                },
                "codCenCusCabCTe": {
                    "$": "F"
                },
                "codCenterResultCte": {
                    "$": "103003"
                },
                "codNatCabCTe": {
                    "$": "F"
                },
                "codNatCte": {
                    "$": "2030000"
                },
                "codProjCabCTe": {
                    "$": "F"
                },
                "codServCabCTe": {
                    "$": "100006"
                },
                "codTipNegCabCTe": {
                    "$": "483"
                },
                "codTipOpCte": {
                    "$": "1607"
                },
                "codTipOperCabCTe": {
                    "$": "1414"
                },
                "codTipTitCte": {
                    "$": "4"
                },
                "consideraICMSXml": {
                    "$": "true"
                },
                "considerarParcDestParcEntrega": {
                    "$": "false"
                },
                "copiaCompradorPedFrete": {
                    "$": "false"
                },
                "copiaCotacaoPedFrete": {
                    "$": "false"
                },
                "copiaObsItemPedFrete": {
                    "$": "false"
                },
                "copiaObsPedFrete": {
                    "$": "false"
                },
                "copiaRateioPedFrete": {
                    "$": "false"
                },
                "criterioRateio": {
                    "$": "V"
                },
                "exigeCteComplementado": {
                    "$": "false"
                },
                "exigePedFrete": {
                    "$": "false"
                },
                "exigeVinculoNota": {
                    "$": "S"
                },
                "importaCabCTe": {
                    "$": "true"
                },
                "importarCTeDocAnterior": {
                    "$": "false"
                },
                "obtencaoCFOP": {
                    "$": "T"
                },
                "permiteSelectParceiroMesmoCnpjCte": {
                    "$": "N"
                },
                "tipoBuscaPedFrete": {
                    "$": "C"
                },
                "tipoDataCte": {
                    "$": "N"
                },
                "tipoImportacaoCabCte": {
                    "$": "C"
                },
                "tolerancia": {
                    "$": "0"
                },
                "vinculaNotaNaoEletronica": {
                    "$": "false"
                },
                "vincularCTeComplOrigem": {
                    "$": "false"
                }
            },
            "paramsNFe": {
                "apuraDivergenciaICMSST": {
                    "$": "N"
                },
                "atualizarCodAnvisa": {
                    "$": "N"
                },
                "atualizarCodEAN": {
                },
                "atualizarInfoCombustivel": {
                    "$": "N"
                },
                "centroDoResultado": {
                    "$": "4"
                },
                "comprador": {
                    "$": "4"
                },
                "considerarCFOPdeBonificacaoImportacaoXML": {
                },
                "considerarValoresIPIDevolVenda": {
                },
                "converterCSTParaCSTAnt": {
                    "$": "N"
                },
                "copiaDeRateio": {
                    "$": "N"
                },
                "desconsiderarValidacao": {
                    "$": "N"
                },
                "dtPrevEntr": {
                    "$": "NOR"
                },
                "filtraSomentePedidos": {
                    "$": "N"
                },
                "gravaChaveRefInexistente": {
                },
                "importarDadosDoInterm": {
                    "$": "N"
                },
                "importarTransportadora": {
                    "$": "S"
                },
                "limiteDivergST": {
                    "$": "0"
                },
                "natureza": {
                    "$": "4"
                },
                "numCotacao": {
                    "$": "4"
                },
                "nuNotaModeloProdutorRural": {
                },
                "observacao": {
                    "$": "5"
                },
                "observacaoItem": {
                    "$": "N"
                },
                "permiteAlteracaoNotaNaCentral": {
                    "$": "S"
                },
                "permiteSelectParceiroMesmoCnpj": {
                    "$": "N"
                },
                "priorizaDescricaoVinculacaoProdutos": {
                    "$": "N"
                },
                "projeto": {
                    "$": "1"
                },
                "qtdDiasDtExtemporaneaCompra": {
                    "$": "0"
                },
                "realizarConvCSTdeIPI": {
                    "$": "N"
                },
                "tipoDeNegociacao": {
                    "$": "4"
                },
                "topSimulacaoNotaCompra": {
                },
                "usarComoDtFaturamento": {
                    "$": "ES"
                },
                "usarTributacaoSistema": {
                    "$": "N"
                },
                "validacaoDoFinanceiro": {
                    "$": "N"
                },
                "validaControleAd": {
                    "$": "S"
                },
                "variacaoMaxQtd": {
                    "$": "0"
                },
                "vinculoManualDevol": {
                    "$": "N"
                }
            },
            "paramsNFeEmissaoPropria": {
                "chkImportarDadosDoInterm": {
                    "$": "N"
                },
                "chkvalidaCadastroParceiroNaImportacaoXML": {
                    "$": "N"
                },
                "codCCus": {
                },
                "codNat": {
                },
                "codProj": {
                },
                "codTipNeg": {
                    "$": "11"
                },
                "codTipOpAjuste": {
                },
                "codTipOpComplemento": {
                },
                "codTipOpCompra": {
                    "$": "1452"
                },
                "codTipOpDevCompra": {
                },
                "codTipOpDevVenda": {
                },
                "codTipOpVenda": {
                    "$": "1800"
                },
                "qtdDiasDtExtemporanea": {
                    "$": "0"
                },
                "validacaoDoFinanceiroEmissaoPropria": {
                }
            },
            "pedidoFreteLigado": {
                "nroPedidoFrete": "",
                "vlrPedidoFrete": ""
            },
            "reprocessar": False,
            "tela": "PORTALIMPORTACAOXML"
        }
    }
    serviceName = "ImportacaoXMLNotasSP.processarArquivo"
    
    r = wrapper.request(
        serviceName=serviceName,
        requestBody=requestBody
    )
    print(r)
    return r

# processarNotaArquivo(12574,12580,12607)