entrada = input()

numString = entrada.split(" ")

numeros = list(map(int, numString))

inicio, fim = numeros

if inicio == fim:
    print("O JOGO DUROU 24 HORA(S)")

if inicio < fim:
    totHora = abs(inicio - fim)
    print("O JOGO DUROU {} HORA(S)".format(totHora))

if inicio > fim:
    totHora = abs((inicio - 24)) + fim
    print("O JOGO DUROU {} HORA(S)".format(totHora))