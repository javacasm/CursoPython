import os
import json


v = '0.4'

baseDir = '/Volumes/myblock/musica/'

nombre_fichero_repetidos = baseDir + 'ficherosRepetidos.json'
nombre_nombre_nombre_fichero_datos = baseDir + 'datos.json'

listaDirectorios = [baseDir]

datos = {}

ficheros = {}

def getInfo(fichero):
    info = os.stat(fichero)
#     print(f'fichero: {fichero} tamaño: {info.st_size}')
    return info

def exploreDir(directorio):
    global listaDirectorios, datos, ficheros
    if directorio[-1] != os.sep:
        directorio += os.sep
        # print(f'ahora {directorio}')
#     print('Explorando ' + directorio)
    for fichero in os.listdir(directorio):
        fullfilename = directorio +  fichero
        if os.path.isdir(fullfilename):
            listaDirectorios.append(fullfilename)
            print(f'Hay {len(listaDirectorios)} pendientes\r')
        else:
            if os.path.isfile(fullfilename):
                info = getInfo(fullfilename)
                if fichero in ficheros:
                    ficheros[fichero].append(fullfilename)
                    print(f'fichero {fichero} repetido {len(ficheros[fichero])} veces' )
                else:
                    ficheros[fichero] = [fullfilename]
                datos[fullfilename] = info.st_size
            else:
                print(f'no se que es {fullfilename}')

def findDuplicates():

    global ficherosRepetidos
    while len(listaDirectorios) > 0:
        directorio = listaDirectorios.pop()
        exploreDir(directorio)
        
    ficherosRepetidos = {}    
    for fichero, listaFicheros in ficheros.items():
        if len(listaFicheros) > 1:
            ficherosRepetidos[fichero] = listaFicheros

    with open(nombre_fichero_repetidos, "wt",encoding='utf-8') as outfile:
        json.dump(ficherosRepetidos, outfile)


    with open(nombre_nombre_nombre_fichero_datos, "wt",encoding='utf-8') as outfile:
        json.dump(datos, outfile)


if os.path.exists(nombre_nombre_nombre_fichero_datos) and os.path.exists(nombre_fichero_repetidos):
    with open(nombre_fichero_repetidos,'rt',encoding='utf-8') as repes:
        ficherosRepetidos = json.load(repes)
    
    with open(nombre_nombre_nombre_fichero_datos,'rt',encoding='utf-8') as dat:
        datos = json.load(dat)
else:
    findDuplicates()
    
print(f'Hay {len(ficherosRepetidos)} ficheros repetidos')
print(f'Hay datos de {len(datos)} ficheros')

def checkDuplicates():
    global ficherosRepetidos
    for repe,lista_repes in ficherosRepetidos.items():
        print(f'{repe} está {len(lista_repes)} veces')
        for fichero_repe in lista_repes:
            print(f'   {fichero_repe} : {datos[fichero_repe]}')

checkDuplicates()