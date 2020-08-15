cont, media = 0, 0
for i in range(6):
    num = float(input())
    if num > 0:
        media += num
        cont += 1
    
print(cont,"valores positivos")
print("{:.1f}".format(media/cont))