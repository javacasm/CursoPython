@app.route("/hola/")
@app.route("/hola/<string:nombre>")
@app.route("/hola/<string:nombre>/<int:edad>")
def hola(nombre = None,edad = None):
    respuesta = '¡¡Hello world!!' 
    if nombre != None and edad != None:
        respuesta =  '¡¡Hola, {}!! Sé que tienes {} años...'.format(nombre,edad)
    elif nombre != None:
        respuesta =  '¡¡Hello, {}!! (también puedes incluir tu edad)'.format(nombre)
    else:
        respuesta = '¡¡Hello world!! (puedes incluir tu nombre y edad)' 
    return  respuesta