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

from ..services.getNuarquivoFromNumnotas import getNuarquivoFromNumnotas
from ..services.processarNotaArquivo import processarNotaArquivo


def launchCTE(numNotas: list):
        
        #
        # SALVAR NUMNOTAS PRA USAR DEPOIS
        #
    # try:
        nuArquivos = getNuarquivoFromNumnotas('01/03/2025',numNotas)
        holding = processarNotaArquivo(nuArquivos)

        processedNotes = holding['avisos']['aviso']

        diverNotes = []

        for n in processedNotes:
            if re.search("Divergência",n["$"]) is not None:
                match = re.search(r'Arquivo:\s*(\d+)',n["$"])
                if match:
                    diverNotes.append(match.group(1))
        print(diverNotes)

        

    # except Exception as e:
    #     print(f"Erro: {e}")
        
    

launchCTE([6332819,6334510,6337246])