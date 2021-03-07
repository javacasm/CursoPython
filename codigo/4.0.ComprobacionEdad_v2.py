strEdad = input('¿Que edad tiene? ')
edad = int(strEdad)
if  edad < 11:
    print('niño')

if edad >=11 and edad <16:
    print('adolescente')

if edad >=16 and edad <25:
    print('joven')

if edad >=25 and edad <65:
    print('maduro')

if edad >=65:
    print('jubilado')