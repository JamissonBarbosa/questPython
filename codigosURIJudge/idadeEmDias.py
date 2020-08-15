entrada = int(input())

tempo = [365, 30]
lista = []

for i in tempo:
    idade = entrada//i
    entrada = entrada%i
    lista.append(idade)
lista.append(entrada)

print(lista[0], "ano(s)")
print(lista[1], "mes(es)")
print(lista[2], "dia(s)")
