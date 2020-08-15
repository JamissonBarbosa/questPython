s= 1
k = 3
d = 2
for i in range(1, 19):
    s+=(k/d)
    k += 2
    d *= 2

print("{:.2f}".format(s))