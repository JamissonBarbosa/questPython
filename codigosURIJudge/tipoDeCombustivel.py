alcool, gasolina, diesel = 0, 0, 0

while True:
    combustivel = int(input())

    if combustivel > 4 or combustivel < 1:
        combustivel = int(input())
    if combustivel == 1:
        alcool += 1
    if combustivel == 2:
        gasolina += 1 
    if combustivel == 3:
        diesel += 1
    if combustivel == 4:
        break

        

print("MUITO OBRIGADO")
print("Alcool:", alcool)
print("Gasolina:", gasolina)
print("Diesel:", diesel)