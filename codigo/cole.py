# Codigo para gestión de un cole


def cargaLista(categoria):
    lista = []

    while True:
        valor = input(categoria + ' ' + str(len(lista) + 1) + ' (ENTER para terminar) ')
        if valor != '':
            lista.append(valor)
        else:
            break
    return lista

alumnos = cargaLista('Alumno')

asignaturas = cargaLista('Asignatura')
notas = []
for asignatura in asignaturas:
    notasAsignatura = []
    for alumno in alumnos:
        notasAsignatura.append(float(input(asignatura + ' de ' + alumno + ' ')))
    notas.append(notasAsignatura)

print(notas)

for j in range(0, len(alumnos)):
    alumno = alumnos[j]
    mensaje = alumno
    for i in range(0, len(asignaturas)):
        asignatura = asignaturas[i]
        mensaje += ' ' + asignatura + ':' + str(notas[i][j])
    print(mensaje)



