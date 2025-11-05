from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, world sss!!</h1>"

@app.route('/info')
def info():
   modulo = "CSS"
   aula = "1" 
   return f"<h1>Modulo: {modulo}, Aula: {aula} </h1>"

