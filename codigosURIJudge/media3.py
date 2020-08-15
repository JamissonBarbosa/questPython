entrada = input()

numString = entrada.split(" ")

numeros = [float(numero) for numero in numString]

n1, n2, n3, n4 = numeros

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print("Media: {:.1f}".format(media))

if media >=7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: {:.1f}".format(notaExame))
    notaFinal = (notaExame + media)/2
    if notaFinal >= 5:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(notaFinal))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(notaFinal))