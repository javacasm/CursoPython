# buscar multiplo de 77 mas cercano y menor que 1000

contador = 1000

repetir = True

while repetir:
    if contador % 77 == 0:
        print(contador)
        repetir = False
    contador -= 1