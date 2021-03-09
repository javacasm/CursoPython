# imprimos el primer multiplo de 77
contador = 1
while contador <= 78:
    if contador % 77 == 0:
        print(contador)
        break
    contador += 1
else:
    print('No hay multiplo')
print('Hemos terminado')