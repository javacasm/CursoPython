# deletrea palabras
cadena = input('Introduzca una palabra ')

for caracter in cadena:
    if caracter == 'l':
        continue  # repetimos desde aqui
    print(caracter)