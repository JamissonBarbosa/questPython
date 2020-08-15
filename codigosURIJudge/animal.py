reino = input()
classe = input()
tipo = input()


retorno = ''
for caractere in reino:
    if caractere.isupper():
        retorno += caractere.lower()
    
reino1 = retorno

retorno1 = ''
for caractere in classe:
    if caractere.isupper():
        retorno1 += caractere.lower()
    
classe1 = retorno1

retorno2 = ''
for caractere in tipo:
    if caractere.isupper():
        retorno2 += caractere.lower()
    
tipo1 = retorno2


if reino1 == 'vertebrado' and classe1 == 'ave' and tipo1 == 'carnivoro':
    print("aguia")

if reino1 == 'vertebrado' and classe1 == 'ave' and tipo1 == 'onivoro':
    print("pomba")

if reino1 == 'vertebrado' and classe1 == 'mamifero' and tipo1 == 'onivoro':
    print("homem")

if reino1 == 'vertebrado' and classe1 == 'mamifero' and tipo1 == 'herbivoro':
    print("vaca")

if reino1 == 'invertebrado' and classe1 == 'inseto' and tipo1 == 'hematofago':
    print("pulga")

if reino1 == 'invertebrado' and classe1 == 'inseto' and tipo1 == 'herbivoro':
    print("lagarta")

if reino1 == 'invertebrado' and classe1 == 'anelideo' and tipo1 == 'hematofago':
    print("sanguessuga")

if reino1 == 'invertebrado' and classe1 == 'anelideo' and tipo1 == 'onivoro':
    print("minhoca")