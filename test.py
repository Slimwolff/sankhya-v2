
def joinNuarquivo(nuarquivo: list) -> list:
    return ",".join(str(element) for element in nuarquivo)

print(joinNuarquivo(['12345',123456]))