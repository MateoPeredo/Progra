from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = ['La guitarra', 'Balada para un gordo']
    return render_template('listar.html', titulo='Canciones', musicas=lista)

app.run(host='0.0.0.0', port=5000)