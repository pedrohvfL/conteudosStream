
from flask import Flask, request, jsonify, render_template

app = Flask("__name__")

@app.route('/home/<int:intVal>')  #conseguimos alterar o tipo da informação se for INTEIRO OU FLOAT
def index(intVal):
    if intVal >= 1:
        return f"Valor positivo: {intVal}"
    else:
        return "Valor negativo"

@app.route('/cadastro/<name>')  #por padrao esta função de rpta dinamica ja peg aa informação como uma STR
def cadastro(name):
    return "seu nome é? {}".format(name)

@app.route('/menu/<produto>')
def visualizacao(produto):
    return "seu produto é {}".format(produto)

@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoa(nome, cidade):
    result = jsonify({'nome':nome, 'cidade':cidade})
    return result
   
if __name__ == '__main__':
    app.run(debug=True)