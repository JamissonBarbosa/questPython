n = int(input())
lista = [0, 1]
fib = ''
for i in range(n):
    num = lista[i] + lista[i+1]
    lista.append(num)
    fib += str(lista[i])+" "  
print(fib[:-1])



