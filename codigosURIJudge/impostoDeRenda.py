renda = float(input())

if renda > 0 and renda <= 2000:
    print("Isento")

if renda > 2000 and renda <= 3000:
    tot = (renda - 2000) * 0.08
    print(tot)

if renda > 3000 and renda <= 4500:
    ir = (renda - 3000)
    tot = (1000*0.08) + ((ir % 500)*0.18)
    print("R$ {:.2f}".format(tot))

if renda > 4500:
    resto = renda - 4500
    print(resto)
    tot = (1000*0.08) + (1500*0.18) + (0.28 * resto)
    print("R$ {:.2f}".format(tot))
    

    