entrada = input()

numstring = entrada.split(" ")

numeros = [int(numero) for numero in numstring]

codigo, quant = numeros

if codigo == 1:
    total = quant*4.00
    print("Total: R$ {:.2f}".format(total))
if codigo == 2:
    total = quant*4.50
    print("Total: R$ {:.2f}".format(total))
if codigo == 3:
    total = quant*5.00
    print("Total: R$ {:.2f}".format(total))
if codigo == 4:
    total = quant*2.00
    print("Total: R$ {:.2f}".format(total))
if codigo == 5:
    total = quant*1.50
    print("Total: R$ {:.2f}".format(total))

