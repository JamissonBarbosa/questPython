entrada = input() 
numerosComoString = entrada.split(" ")

numeros = [float(numero) for numero in numerosComoString] 

codigo1, num1, valor1 = numeros

entrada = input() 
numerosComoString = entrada.split(" ")

numeros = [float(numero) for numero in numerosComoString] 

codigo2, num2, valor2 = numeros

total = (num1*valor1) + (num2 * valor2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))