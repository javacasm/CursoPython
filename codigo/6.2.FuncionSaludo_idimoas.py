def saludo(nombre = 'Python'):
    '''
    Muestra un saludo en pantalla
    
    param nombre: a quien saludamos
    '''
    global idioma
    idioma = 'en'
    if  idioma =='es':
        print(f'Hola {nombre}')
    else:
        print(f'Hello {nombre}')
    
idioma = 'es'
saludo('Juan')
