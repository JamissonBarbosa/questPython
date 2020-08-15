n = int(input())

for i in range(n):
    x = int(input())

    if x == 0:
        print("NULL")
    else:
        if x % 2 == 0:
            if x > 0:
                print("EVEN POSITIVE")
            if x < 0:
                print("EVEN NEGATIVE")
        if x % 2 == 1:
            if x > 0:
                print("ODD POSITIVE")
            if x < 0:
                print("ODD NEGATIVE")
    
        