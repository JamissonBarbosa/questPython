
entrada = input().split(" ")
PA, PB, G1, G2 = map(float, entrada)
cont, soma = 0, 0
for i in range(100):
   
    if PA < PB:
        taxaA = round(PA * (G1/100))
        taxaB = round(PB * (G2/100))
        PB += taxaB
        PA += taxaA
        cont +=1
    
print(cont, "anos.", PA)
    

