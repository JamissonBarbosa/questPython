salario = float(input())

if salario > 0 and salario <= 400.00:
    reajuste = (salario * 0.15)
    salario1 = salario + reajuste
     
    print("Novo salario: {:.2f}".format(salario1))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 15 %")

if salario > 400.00 and salario <= 800.00:
    reajuste = (salario * 0.12)
    salario1 = salario + reajuste 
    
    print("Novo salario: {:.2f}".format(salario1))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 12 %")

if salario > 800.00 and salario <= 1200.00:
    reajuste = (salario * 0.10) 
    salario2 = salario + reajuste
    
    print("Novo salario: {:.2f}".format(salario2))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 10 %")

if salario > 1200.00 and salario <= 2000.00:
    reajuste = (salario * 0.07)
    salario3 = salario + reajuste
    
    print("Novo salario: {:.2f}".format(salario3))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 7 %")

if salario > 2000.00:
    reajuste = (salario * 0.04)
    salario4 = salario + reajuste 
    
    print("Novo salario: {:.2f}".format(salario4))
    print("Reajuste ganho: {:.2f}".format(reajuste))
    print("Em percentual: 4 %")