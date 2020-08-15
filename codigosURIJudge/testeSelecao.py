entrada = input()

numString = entrada.split(" ")

numeros = [int(numero) for numero in numString]

a, b, c, d = numeros

somacd = c + d
somaba = a + b
par = a%2

if b > c and d > a and somacd > somaba and c >= 0 and d >= 0 and (par == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")