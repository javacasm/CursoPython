import os

listaDirectorios = ['./Descargas']

def showInfo(fichero):
    info = os.stat(fichero)
    print(f'fichero: {fichero} tamaño: {info.st_size}')

def exploraDir(directorio):
    global listaDirectorios
    print('Explorando ' + directorio)
    for fichero in os.listdir(directorio):
        if os.path.isdir(fichero):
            listaDirectorios.append(fichero)
        if os.path.isfile(fichero):
            showInfo(fichero)

while len(listaDirectorios) > 0:
    directorio = listaDirectorios.pop()
    exploraDir(directorio)
    
    
        