# Pega Nuarquivos pelo numero das notas
# Processar arquivos em lotes
# Pega NUARQUIVO
# Pega Divergencias ligadas ao NUARQUIVO
# Executa Botão de ação com numero unico das divergencias
# valida importação de cada NUARQUIVO
# troca parceiro caso necessario
# confirma nota
# renegoceia titulo com numero do documento informado
import json
import re

from ..services.getConfigFromNuarquivo import getConfigFromNuarquivo
from ..services.validaXMLNuarquivo import checkValidacoes
from ..services.getNuarquivoFromNumnotas import getNuarquivoFromNumnotas
from ..services.processarNotaArquivo import processarNotaArquivo
from ..services.actionButton import actionButton
from ..services.pesquisaPedidoLivroFiscal import pesquisaPedidoLivroFiscal
from ..services.removePedidoLivroFiscal import removePedidoLivroFiscal

def getNroUnicoFromConfig(nuarquivo: list) -> list:
    '''
        Pega nro unico das msg dentro das validacoes \n
        Retorna lista de nro(s) unico(s).
    '''
    holdingConfig = getConfigFromNuarquivo(nuarquivo)

    result = []

    # remove \n before checkValidacoes
    holdValidacoes = []
    for h in holdingConfig:
        st = h[1].replace("\n", "")
        holdValidacoes.append(st)

    for n in holdValidacoes:
        chkVal = checkValidacoes(n)
        print(chkVal)
        match = re.findall(r"(\d{6,}){1,}", chkVal)
        for m in match:
            result.append(m)
        
    return result

def mudaFrete(nroNotas: list):
    r = actionButton(146, {
                "type": "S", 
                "paramName": "NUNOTA", 
                "$": nroNotas 
            }
        )
    return r

def getChaveRelacionadaFromConfig():
    pass


def launchCTE(numNotas: list):
        
        #
        # SALVAR NUMNOTAS PRA USAR DEPOIS
        #
    # try:

        #PROCESSAR NOTAS
        nuArquivos = getNuarquivoFromNumnotas('01/03/2025',numNotas)

        # print(f"ISTO SÃO OS NUARQUIVOS INIT: ---------------- {nuArquivos}")

        holding = processarNotaArquivo(nuArquivos)

        #PEGA NOTAS COM DIVERGENCIAS
        processedNotes = holding['avisos']['aviso']
        diverNotes = []
        for n in processedNotes:
            if re.search("Divergência",n["$"]) is not None:
                match = re.search(r'Arquivo:\s*(\d+)',n["$"])
                if match:
                    diverNotes.append(int(match.group(1)))
        print(diverNotes)

        #PEGA NUMERO UNICO DAS NOTAS RELACIONADAS QUE ESTAO COM DIVERGENCIA
        nroUniqs = getNroUnicoFromConfig(diverNotes)        

        print(f"NUMERO UNICOS +============== \n {nroUniqs}")

        # PESQUISA OS NRO UNICOS QUE ESTAO EM nroUniqs E REMOVE CASO ESTEJA NO LIVRO FISCAL
        for nr in nroUniqs:
            r = pesquisaPedidoLivroFiscal(""+nr)
            if r != []:
                pks = []
                for pk in r:
                    pks.append({
                        "NUNOTA": pk[0],
                        "ORIGEM": pk[1],
                        "SEQUENCIA": pk[2],
                        "CODEMP": pk[3]
                    })
                
                removePedidoLivroFiscal(pks=pks)
            else:
                print("numero unico nao esta no livro fiscal")
        

        # CONCATENA OS NRO UNICOS EM UMA STRING PARA USAR O BOTAO DE ACAO
        strNroUniq = ""

        for index, nro in enumerate(nroUniqs):
            if index != len(nroUniqs)-1:
                strNroUniq = strNroUniq + nro + ","
            else:
                strNroUniq = strNroUniq + nro
        
        action = actionButton(id=146,param=[{"type": "S", "paramName": "NUNOTA", "$": strNroUniq }])
        print(action)

        # VALIDA IMPORTAÇÃO DE CADA NUARQUIVO
        nuArquivoFinal = []

        # for nu in nuArquivos:


    # except Exception as e:
    #     print(f"Erro: {e}")
        
    

launchCTE([
6336484
])

# getNroUnicoFromConfig([12685])