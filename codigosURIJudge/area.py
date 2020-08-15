entrada = input() 
numerosComoString = entrada.split(" ")

numeros = [float(numero) for numero in numerosComoString] 


a, b, c = numeros

triangulo = (a * c) / 2
print("TRIANGULO: {:.3f}".format( triangulo))

circulo = (3.14159 * c**2 )
print("CIRCULO: {:.3f}".format( circulo))

trapezio = ((a + b) * c) / 2
print("TRAPEZIO: {:.3f}".format( trapezio))

quadrado = b * b
print("QUADRADO: {:.3f}".format( quadrado))

retangulo = a * b
print("RETANGULO: {:.3f}".format( retangulo))