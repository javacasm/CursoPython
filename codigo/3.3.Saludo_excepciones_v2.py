nombre = input('¿Como te llamas? ')
print('Hola ', nombre)
strEdad = input('¿Cuantos años tienes? ')

try:
    edad = int(strEdad)
    print('Tienes ',edad,' años')
    nacimiento = 2021 - edad
    print('Naciste en el año ',nacimiento)
except:
    print('Se ha producido un error en la conversion')

print('Adios') 