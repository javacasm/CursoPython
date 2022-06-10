from flask import Flask

app = Flask("Ejemplo inicial con flask")

@app.route('/')
def index():
    return "Hola Flask"

if __name__ == '__main__':
    app.run(debug = False, host='0.0.0.0')