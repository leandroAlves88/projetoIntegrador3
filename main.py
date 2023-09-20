from flask import Flask, render_template, request, redirect
import buscador

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resultado',methods=['POST'])
def resultados():
    campo_busca = request.form['txtBusca']

    print(f'campo pesquisar: {campo_busca}')
    buscador.motor_busca(campo_busca)
        #return redirect(request.url)
    #return f'O valor do campo é: {campo_busca}'

    return render_template('resultado.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)