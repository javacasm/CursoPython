strEdad = input('¿Que edad tiene? ')
edad = int(strEdad)
if  edad < 11:
    print('niño')
elif edad <16:
    print('adolescente')
elif edad <25:
    print('joven')
elif edad <65:
    print('maduro')
else:
    print('jubilado')