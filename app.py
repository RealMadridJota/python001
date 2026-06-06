from flask import Flask

app = Flask(__name__)

@app.route('/')

def hola_mundo():
    return '<H1>Hola mundo<H1>'

if __name__ == '__main__':
    app.run(debug=True)
    
#comentario para guardar el cambio