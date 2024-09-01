import leitor, moinho, impressora

codigo, posicao, numeros = (leitor.ler_cartao("cartao.in"))
for c in range(0,len(codigo)):
    moinho.decifrar(codigo[c], posicao[c],numeros[c])

impressora.cartao.close()
