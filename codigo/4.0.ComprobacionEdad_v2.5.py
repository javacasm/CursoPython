strEdad = input('¿Que edad tiene? ')
edad = int(strEdad)
if  edad < 11:
    print('niño')

if 11 <= edad <16:
    print('adolescente')

if 16 <= edad <25:
    print('joven')

if 25 <= edad <65:
    print('maduro')

if edad >=65:
    print('jubilado')