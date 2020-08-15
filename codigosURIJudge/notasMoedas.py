valor = float(input())

notas = [100, 50, 20, 10, 5, 2, 1.00, 0.5, 0.25, 0.10, 0.05, 0.01]
lista = []

for nota in notas:
    while nota > 1:
        quant = valor//nota
        print("{:.0f} nota(s) de R$ {}.00".format(quant, nota))
        valor %= nota
        nota = nota

    quant = valor//nota
    print(int(quant), "moeda(s) de R$", nota)
    valor %= nota

