# Simulación de consola de comandos v3
usuario = input('Introduzca el nombre de usuario: ')
if usuario == 'pepe' or usuario == 'admin':
    print('Bienvenido ' + usuario)
    comando = input('Introduzca el comando: ')
    if comando == 'Apagar':
        confirmacion = input('Confirme que desea apagar respondiendo "Si": ' )
        if confirmacion == 'Si':
            print('Apagando el equipo...')
        else:
            print('No se ha confirmado el apagado')
    elif comando == 'Encender':
        print('Encendemos el equipo')
    else :
        print('Comando ' + comando + ' no reconocido')
else:
    print('Acceso denegado')