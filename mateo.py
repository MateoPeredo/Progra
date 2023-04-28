from flask import Flask, render_template

class Cancion:
    def __init__(self,titulo,categoria,idioma):
        self.titulo=titulo
        self.categoria=categoria
        self.idioma=idioma
        
app = Flask(__name__)

@app.route('/')
def index():
    cancion1 = Cancion('La guitarra', 'Pop', 'Castellano')
    cancion2 = Cancion('Wait and bleed', 'Metal', 'Ingles')
    cancion3 = Cancion('Balada para un gordo', 'Rock', 'castellano')
    lista = [cancion1, cancion2, cancion3]
    return render_template('listar.html', titulo='Canciones', musicas=lista)
    
    @app.route('/nuevoregistro')
    def nuevoregistro():
        return render_template('nuevoRegistro.html', titulo='Nueva cancion')
app.run(host='0.0.0.0', port=5000)



