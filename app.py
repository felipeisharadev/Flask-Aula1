from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Olá, Mundo !"

@app.get("/info") 
def info(): 
   modulo = "Flask" 
   aula = 1
   return f"Módulo: {modulo} — Aula {aula}"