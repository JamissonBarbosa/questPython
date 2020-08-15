while True:
    entrada = input().split(" ")
    numeros = map(int, entrada)
    x, y = numeros
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
    else:
        break
    