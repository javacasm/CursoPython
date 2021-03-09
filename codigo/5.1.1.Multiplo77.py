# buscar multiplo de 77 mas cercano y menor que 1000

contador = 1000

while True:  # bucle infinito
    if contador % 77 == 0:
        print(contador)
        break
    contador -= 1
