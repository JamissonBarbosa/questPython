t = int(input())

cont = 0
if t >= 2 and t <= 50:
    for i in range(1000):
        for j in range(t):
            print('N[{}] = {}'.format(cont, j))
            cont += 1
