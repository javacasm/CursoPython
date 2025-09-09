#Ejemplo petición de datos correctos al usuario
pedirDatos = True
while pedirDatos:
    try:
        datoStr = input('Dame el número: ')
        datoInt = int(datoStr)
        # si llega aquí es que no ha saltado la excepción
        pedirDatos = False
    except: # ha ocurrido un error
        print('Debes dar un número entero válido')
print(f'Dato introducido {datoInt} ')
