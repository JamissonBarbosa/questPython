result = ''
while True:
    x = int(input())
    if x == 0:
        break
    else:
        for i in range(1, x+1):
            result += str(i) + " "
        print(result[:-1])
        result = ''