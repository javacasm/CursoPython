strEdad = input('¿Que edad tiene? ')
edad = int(strEdad)
if  edad < 11:
    print('niño')
else:
    if edad <16:
        print('adolescente')
    else:
        if edad <25:
            print('joven')
        else:
            if edad <65:
                print('maduro')
            else:
                print('jubilado')