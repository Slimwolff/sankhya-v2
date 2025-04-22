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
from ..services.validaXMLNuarquivo import checkMsgNroUnico, checkChaveReferenciada
from ..services.getNuarquivoFromNumnotas import get_nuarquivo_from_numnotas
from ..services.processarNotaArquivo import processarNotaArquivo
from ..services.actionButton import actionButton
from ..services.pesquisaPedidoLivroFiscal import pesquisaPedidoLivroFiscal
from ..services.removePedidoLivroFiscal import removePedidoLivroFiscal
from ..services.validarImportacaoXML import validarImportacaoXML

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

    for index, n in enumerate(holdValidacoes):
        chkVal = checkMsgNroUnico(n)
        print(f"index: {index} | chkVal:  {chkVal}")
        if chkVal is not None:
            # print(chkVal)
            match = re.findall(r"(\d{6,}){1,}", chkVal)
            for m in match:
                result.append(m)
        
    return result

def mudaFrete(nroUnico: str) -> dict:
    return actionButton(id=146,param=[{"type": "S", "paramName": "NUNOTA", "$": nroUnico }])

def nroUnicoListToString(nroUniqs: list):
    
    s = ""
    if not nroUniqs:
        return ""
    
    for i, nro in enumerate(nroUniqs):
        if i != len(nroUniqs)-1:
            s = s + nro + ","
        else:
            s = s + nro
    return s

def getDivergenceFromWarning(processedNotes: list | dict):
    """
        Retorna lista com nuarquivos
    """
    d = []

    if type(processedNotes) == dict:
        if re.search("Divergência",processedNotes["$"]) is not None:
            match = re.search(r'Arquivo:\s*(\d+)',processedNotes["$"])
            if match:
                d.append(int(match.group(1)))
    else:
        for n in processedNotes:
            if re.search("Divergência",n["$"]) is not None:
                match = re.search(r'Arquivo:\s*(\d+)',n["$"])
                if match:
                    d.append(int(match.group(1)))
    return d


def launchCTE(numNotas: list):


        # PEGAS NUNOTA NUARQUIVO E NUMNOTAS
        NUARQUIVOS = get_nuarquivo_from_numnotas(numNotas)

        # VERIFICA QUAIS JA TEM NOTA E ADICIONA OS QUE NAO TEM PARA SEREM PROCESSADOS
        narq = []
        for na in NUARQUIVOS:
            if not na[0]:
                narq.append(na[1])


        holding = processarNotaArquivo(narq)

        #PEGA NOTAS COM DIVERGENCIAS

        if 'aviso' in holding:
            processedNotes = holding['aviso']['AVISO']
        else:
            processedNotes = holding['avisos']['aviso']
        

        
        notas_com_divergencia = getDivergenceFromWarning(processedNotes)

        #PEGA NUMERO UNICO DAS NOTAS RELACIONADAS QUE ESTAO COM DIVERGENCIA
        nroUniqs = getNroUnicoFromConfig(notas_com_divergencia)        


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
        strNroUniq = nroUnicoListToString(nroUniqs=nroUniqs)

        # MUDA FRETE INCLUSO PARA EXTRA NOTA COM O BOTÃO DE AÇÃO
        action = mudaFrete(strNroUniq)
        print(action)

        # VALIDA IMPORTAÇÃO DE CADA NUARQUIVO
        nuArquivoFinal = []
        for nd in numNotas:
        
            config = getConfigFromNuarquivo([nd])

            nuArquivoFinal.append({
                "NUARQUIVO": nd,
                "CHAVEREFERENCIADA": checkChaveReferenciada(config[0][1])
            })
        

        for nuaf in nuArquivoFinal:
            imp = validarImportacaoXML(nuaf['NUARQUIVO'], nuaf['CHAVEREFERENCIADA'])
            print(imp)

        

        
    

# launchCTE([
# 70006
# ])

# getNroUnicoFromConfig([12685])

# def removeFromLivroFiscal(nuarquivo: list):
#     nroUniqs = getNroUnicoFromConfig(nuarquivo)  
#     print(nroUniqs)
#     for nr in nroUniqs:
#             r = pesquisaPedidoLivroFiscal(""+nr)
#             if r != []:
#                 pks = []
#                 for pk in r:
#                     pks.append({
#                         "NUNOTA": pk[0],
#                         "ORIGEM": pk[1],
#                         "SEQUENCIA": pk[2],
#                         "CODEMP": pk[3]
#                     })
                
#                 removePedidoLivroFiscal(pks=pks)
#             else:
#                 print("numero unico nao esta no livro fiscal")

def processaNotaFromNumnotas(numNotas: list):

    nuArquivoFinal = []
    for nd in numNotas:
        
        config = getConfigFromNuarquivo([nd])

        

        nuArquivoFinal.append({
            "NUARQUIVO": nd,
            "CHAVEREFERENCIADA": checkChaveReferenciada(config[0][1])
        })
        print(nuArquivoFinal[0])

    

processaNotaFromNumnotas([13499])