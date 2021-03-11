def saludo(nombre = 'Python', idioma = 'en'):
    '''
    Muestra un saludo en pantalla
    
    param nombre: a quien saludamos
    '''


    if  idioma =='es':
        print(f'Hola {nombre}')
    else:
        print(f'Hello {nombre}')
    
idioma = 'es'
saludo('Juan',idioma)
saludo(nombre='Manolo', idioma='en')
saludo(idioma='es', nombre='Felipe')
