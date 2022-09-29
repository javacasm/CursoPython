from datetime import datetime
nacimiento = datetime(1970,12,25,15,0,0) # Fecha y hora de nacimiento
hoy = datetime.now()
diferencia = hoy - nacimiento
print(f'han pasado {diferencia}')

print(f'tienes {diferencia.days} días, y {diferencia.seconds} segundos')
horas = diferencia.seconds // 3600 # segundos que tiene 1 hora
restoSegundos = diferencia.seconds - horas * 3600
minutos = restoSegundos // 60
segundos = restoSegundos - minutos * 60
print(f'o {diferencia.days} días, {horas} horas, {minutos} minutos y {segundos} segundos')

