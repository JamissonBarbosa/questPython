entrada = input()

numString = entrada.split(" ")

numeros = list(map(int, numString))

i, mi, f, mf = numeros

if i == f:
    if mi < mf:
        H = 0
        M = mf - mi
    elif mi > mf:
        H = 23
        M = 60 - (mi - mf)
    else:
        H = 24
        M = 0

elif i < f:
    H = f - i
    if mi > mf:
        M = mi - mf
        if mi - mf == 1:
            H = 0
            M = 59
        elif (f - i) == 2:
            H = 1
            M = 60 - M
    elif mi < mf:
        M = mf - mi
    else:
        M = 0
else:
    H = 24 - (i - f)
    if (i - f) == 1 and mi > mf:
        H = 22
        M = 60 - (mi -mf)
    elif mi > mf:
        if mf == 0:
            M = mi
        elif mi <= 30 and mf <= 30:
            M = M = mi - mf
        else:
            M = 60 - (mi - mf)
    elif mi < mf:
        M = mf - mi
    else:
        M = 0
        H = 23

print('O JOGO DUROU %d HORA(S) E %d MINUTO(S)' %(H, M))