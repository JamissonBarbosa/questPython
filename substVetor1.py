x =[]

for i in range(10):
    num = int(input())
    x.append(num)

for i in range(len(x)):
    if x[i] <= 0:
        x[i] = 1
    print("X[{}] = {}".format(i, x[i]))