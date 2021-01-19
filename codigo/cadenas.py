cadena = "Recipe 5: Rewriting, and the Immutable String"

## método 1

partesCadena = cadena.split(':')
cadena2 = partesCadena[1]
cadena3 = cadena2.replace(',','_')
cadena4 = cadena3.replace(' ','_')
print(cadena4)

## método 2
bAntesDe2Puntos = True
cadenafinal = ''
for char in cadena:
    if bAntesDe2Puntos == False:
        if char == ' ' or char == '':
            cadenafinal += '_'
        else:
            cadenafinal += char

    if char == ':' :
        bAntesDe2Puntos = False
    
print(cadenafinal)

## método 3

cadena2 = cadena.replace('Recipe 5:','')
cadena3 = cadena2.replace(',','_')
cadena4 = cadena3.replace(' ','_')

print(cadena4)

## metodo 4

division = cadena.split()
quitar = division[2:]

quitar[0] = 'Rewriting'

resultado = '_'.join(quitar)
print(resultado)




