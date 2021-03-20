from random import randint
palos = "♠ ♡ ♢ ♣".split()
numeros = "2 3 4 5 6 7 8 9 10 J Q K A".split()

carta =''' ___
|{n: <2s} |
| {s} |
|_{n:_>2s}|'''

def muestraTodas():
    for s in palos:
        for n in numeros:
            print(carta.format(n=n,s=s))
        
        
carta2 = (' ___ ','|{n: <2s} |','| {s} |','|_{n:_>2s}|')

def muestraTodas2():
    for s in palos:
        for ss in carta2:
            for n in numeros:
                print(ss.format(n=n,s=s), end=' ')
            print('')
        print('')

def creaMano():
    mano = []
    for _ in range(5):
        s = palos[randint(0,len(palos))-1]
        r = numeros[randint(0,len(numeros))-1]
        mano.append(f'{s}{r}')
    return mano

def muestraMano(mano):
    for ss in carta2:
        for naipe in mano:
            print(ss.format(n=naipe[1:],s=naipe[0]), end=' ')
        print('')

for _ in range(100):
    mano = creaMano()
    # print(mano)
    muestraMano(mano)

