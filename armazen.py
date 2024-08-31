memoria = [0] * 16
def armazenar(valor, posicao):
    memoria[posicao] = valor
    return memoria

def carregar(posicao):
    return memoria[posicao]
