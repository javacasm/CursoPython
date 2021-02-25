# Pagina web con flask

from flask import Flask, request

app = Flask('Hello Flask')

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/test')
def test():
    return 'test Flask'

if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1') # solo acceso local y puerto 5000

