# Tarea 2/3
"""
 Ejemplo de uso de listas, entrada de datos del usuario
 Codigo para gestión de las notas de un cole
 Se piden primero los nombres de los alumnos (nombre vacío para terminar)
 Se piden después las asignaturas (asignatura vacía para terminar)
 Después se piden las notas

 License CC by SA
 by @javacasm

 6/4/2020

"""

def cargaLista(categoria):
    lista = []

    while True:
        valor = input(categoria + ' ' + str(len(lista) + 1) + ' (ENTER para terminar) ')
        if valor != '':
            lista.append(valor)
        else:
            break
    return lista

# Vamos a pedir los nombres de los alumnos
alumnos = cargaLista('Alumno')

# Vamos a pedir los nombres de las asignaturas
asignaturas = cargaLista('Asignatura')
notas = []

# Vamos a pedir las notas
for asignatura in asignaturas:
    notasAsignatura = []
    for alumno in alumnos:
        notasAsignatura.append(float(input(asignatura + ' de ' + alumno + ' ')))
    notas.append(notasAsignatura)

# print('Las notas son: ',notas)

# Mostrar todas las notas
for j in range(0, len(alumnos)):
    alumno = alumnos[j]
    mensaje = alumno
    for i in range(0, len(asignaturas)):
        asignatura = asignaturas[i]
        mensaje += ' ' + asignatura + ':' + str(notas[i][j])
    print(mensaje)

# Medias por alumno
for j in range(0, len(alumnos)):
    alumno = alumnos[j]
    mensaje = alumno
    suma = 0
    for i in range(0, len(asignaturas)):
        suma += notas[i][j]
    media = suma / len(asignaturas)
    mensaje += ' tiene una media de ' + str(round(media * 100)/100) # Para redondear a 2 decimales
    print(mensaje)

# Medias por asignatura
for i in range(0, len(asignaturas)):
    asignatura = asignaturas[i]
    mensaje = 'En la asignatura ' + asignatura
    suma = 0
    for j in range(0, len(alumnos)):
        suma += notas[i][j]
    media = suma / len(alumnos)
    mensaje += ' la media es ' + str(round(media * 100)/100) # Para redondear a 2 decimales
    print(mensaje)





