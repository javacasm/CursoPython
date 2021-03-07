nombre = input('¿Como te llamas? ')
print(f'Hola {nombre}')
strEdad = input('¿Cuantos años tienes? ')

try:
    edad = int(strEdad)
    cadena = f'Tienes {edad} años y naciste en el año {2021 - edad}'
    print(cadena)
except:
    print('Se ha producido un error en la conversion')

print('Adios')