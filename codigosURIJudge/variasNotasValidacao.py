media, cont = 0, 0
while True:
    notas = float(input())

    if notas >= 0 and notas <= 10:
        media += notas
        cont += 1
        if cont == 2:
            print("media = {:.2f}".format(media/2))
            if cont == 2:
                print("novo calculo (1-sim 2-nao)")
                proc = int(input())
                if proc == 1:
                    cont, media = 0, 0
                    continue
                elif proc == 2:
                    break
                else:
                    while proc != 1 and proc != 2:
                        print("novo calculo (1-sim 2-nao)")
                        proc = int(input())
                
                cont, media = 0, 0

    else:
        print("nota invalida")
