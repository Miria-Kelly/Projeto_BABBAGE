cartao = open('cartao.out', 'w')
def escrever(valor):

    valor = bin(valor)[2:]
    valor = str(valor)
    o_que_falta = 4 - (len(valor) % 4)
    cartao.write("OOOO OOOO ")
    if o_que_falta != 0:
        for c in range(0, o_que_falta):
            valor = '0' + valor
    for c in valor:
        if c == '1':
            valor = valor.replace("1", "X")

        else:
            valor = valor.replace('0', 'O')
    tam = len(valor)
    cont = 0

    for c in valor:
        cont += 1
        cartao.write(c)
        if cont % 4 == 0 and cont != tam:
            cartao.write(' ')

    cartao.write('\n')

