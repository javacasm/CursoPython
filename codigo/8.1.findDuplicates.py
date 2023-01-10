import os

v = '0.1'

listaDirectorios = ['/media/myBlock/musica']

datos = {}

def getInfo(fichero):
    info = os.stat(fichero)
    print(f'fichero: {fichero} tamaño: {info.st_size}')
    return info

def exploreDir(directorio):
    global listaDirectorios, data
    if directorio[-1] != os.sep:
        directorio += os.sep
        # print(f'ahora {directorio}')
    print('Explorando ' + directorio)
    for fichero in os.listdir(directorio):
        fullfilename = directorio +  fichero
        if os.path.isdir(fullfilename):
            listaDirectorios.append(fullfilename)
            print(f'añadido dir {fichero}')
        else:
            if os.path.isfile(fullfilename):
                info = getInfo(fullfilename)
                if fichero in datos.keys():
                    print(f'fichero {fichero} repetido' )
                else:
                    datos[fichero] = info
            else:
                print(f'no se que es {fullfilename}')

while len(listaDirectorios) > 0:
    directorio = listaDirectorios.pop()
    exploreDir(directorio)
    
    
        
