# Programa que determina si un año es o no bisiesto
year = int(input('Introduzca el año: '))
if ((year%400)==0  or (year % 100) ==0 or (year%4)==0): # la regla para saber si es bisiesto
  print('Es bisiesto!!')
else:
  print ('No es bisiesto!!')
