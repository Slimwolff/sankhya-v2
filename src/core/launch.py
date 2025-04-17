
from ..services.getNuarquivoFromNumnotas import getNuarquivoFromNumnotas


def getCte(numnotas: list):

    nuarquivo = []

    for num in numnotas:
        n = getNuarquivoFromNumnotas('01/03/2025',[num])
        if not n:
            print("numnota não encontrada")
        else:
            nuarquivo.append(n[0])

    print(f"nuarquivos: {nuarquivo}")


getCte([
    438758,
6332819,
6332829,
6332837,
6334238,
6334508,
6334510,
6334513,
6334515,
6336323,
6336484,
6337246,
6337250,
6337283,
6337297,
6337294,
6338056,
6338067,
6338091,
195785,
6340247,
6340635,
6340725,
6340772,
6341248,
18458,
6343756,
6343767,
6343884,
6344156,
6344161,
6344366,
6345521,
6345639,
6345647,
6345655,
958230,
6349332,
6349337,
6349396,
6349495,
6350578,
2559032
])