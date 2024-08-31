def ler_cartao(cartao_entrada):
    with open(cartao_entrada, 'r') as cartao:
        linhas = cartao.read()

        for c in linhas:
            if c == "X":
                linhas = linhas.replace("X", "1")

            else:
                linhas = linhas.replace("O", "0")
        cont = 0
        tam = len(linhas.split())
        if tam > 4:
            linhas = linhas.split('\n')
            linhas2 = []
            for c in range(0,len(linhas)):
                linha = linhas[c].split()
                linhas2.append(linha)
                cont += 1

            codigo = []
            posicao = []
            numeros = []
            for c in linhas2:
                codigo.append(c[0])
                posicao.append(c[1])
                numeros.append(c[2:])
            numeros_convertidos = []
            posicao_convertida = []
            numeros1 = [''.join(sublista) for sublista in numeros]

            for sublista in posicao:
                posicao_convertida.append(int(sublista, 2))

            for sublista in numeros1:
                numeros_convertidos.append(int(sublista, 2))

            return codigo, posicao_convertida, numeros_convertidos

        else:
            linhas = linhas.split()
            codigo = linhas[0]
            posicao = linhas[1]
            numeros = linhas[2:]

            i =''
            for c in numeros:
                i += c
            numeros_convertidos = int(i, 2)
            posicao_convertida = int(posicao, 2)

            return codigo, posicao_convertida, numeros_convertidos





