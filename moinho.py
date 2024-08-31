import armazen, impressora
valores = []
valor = 0
def decifrar(codigo, posicao, numero):
    global resultado
    if codigo == "0001":
        memoria = armazen.armazenar(numero, posicao)
        return memoria

    elif codigo == "0010":
        num = armazen.carregar(posicao)
        valores.append(num)
        return valores

    elif codigo == "0011":

        resultado = valores[0] + valores[1]
        return resultado

    elif codigo == '0100':

        resultado = valores[0] - valores[1]
        return resultado

    elif codigo == "0101":

        resultado = valores[0] * valores[1]
        return resultado

    elif codigo == "0110":
        return armazen.armazenar(resultado, posicao)

    elif codigo == "0111":
        global valor
        valor = armazen.carregar(posicao)
        return impressora.escrever(valor)












"""def LOADOP(valor, posicao):
    #carrega valor na posicao da memoria fornecida

def ADD(a, b):
    #soma dois operadnos que foram carregados no moinho

def SUB(a, b):
    #subtrai os dois valores que foram carregados no moinho

def MUL(a, b):
    #multiplica  os dois valores que forams careegados no moinho

def STORE(resultado):
    #armazena o resultado ultima operaçao realizada no moinho

def PRINT(valor):
    #escreve o conteudo da posicao dada do armazem"""