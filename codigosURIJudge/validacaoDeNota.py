media, cont = 0, 0
while True:
    notas = float(input())

    if notas >= 0 and notas <= 10:
        media += notas
        cont += 1
        if cont == 2:
            print("media =",media/2)
            break
    else:
        print("nota invalida")
