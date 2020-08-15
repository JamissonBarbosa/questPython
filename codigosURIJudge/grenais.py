grenais, vicInter, vicGremio, empates = 0, 0, 0, 0

while True:
    entrada = input().split()
    numeros = map(int, entrada)
    inter, gremio = numeros

    if inter > gremio:
        vicInter += 1
        grenais += 1
    if inter < gremio:
        vicGremio += 1
        grenais += 1
    if inter == gremio:
        empates += 1
        grenais += 1

    print("Novo grenal (1-sim 2-nao)")
    continuar = int(input())

    if  continuar == 1:
        continue
    if continuar == 2:
        print(grenais,"grenais")
        print("Inter:{}".format(vicInter))
        print("Gremio:{}".format(vicGremio))
        print("Empates:{}".format(empates))
        if vicInter > vicGremio:
            print("Inter venceu mais")
        elif vicInter < vicGremio:
            print("Gremio venceu mais")
        else:
            print("Nao houve vencedor")
        break
