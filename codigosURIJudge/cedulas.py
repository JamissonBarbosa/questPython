N = int(input()) 

notas = [100,50,20,10,5,2,1]

print(N)
for x in notas:
    print ("{} nota(s) de R$ {},00".format((N//x),x))
    N %= x