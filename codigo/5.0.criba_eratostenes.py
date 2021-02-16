"""

 Criba de Eratóstenes

 Se van retirando la lista todos los múltiplos conocidos de cada número

 License CC by SA
 by @javacasm

 9/4/2020

"""

N = 10000  # Hasta donde haremos la criba

# empezamos con todos los números
# criba = [x for x in range(2, N + 1)]

print('Cálculo de número primos hasta el %d usando el método de la criba de Eratóstenes' %N)

criba = list(range(2, N + 1))

posicion = 0

def retiraMultiplos():
    global posicion, criba, N

    elemento = criba[posicion]

    if elemento*elemento > N:
        print('Hemos  terminado')
        print('criba (%d): ' % len(criba), criba)
        return 0

    multiplos = [elemento * x for x in range(2, N//elemento + 1)]
    print('múltiplos de ', elemento, ' (%d)' % len(multiplos))
    # print('múltiplos de ', elemento, ':', multiplos)

    for multiplo in multiplos:
        if criba.count(multiplo):   # numero está en criba
            criba.remove(multiplo)  # lo quitamos
    posicion += 1
    print('criba (%d): ' % len(criba))
    # print('criba (%d): ' % len(criba), criba)
    return len(criba)

while retiraMultiplos() > 0:
    pass
