from flask import Flask, render_template, request, redirect
import buscador

app = Flask(__name__)


@app.route("/")
def home():
    """
    Essa função tem o objetivo de iniciar chamando a pagina princial.
    """
    return render_template("home.html")


@app.route("/resultado", methods=["POST"])
def resultados():
    """
    Essa função tem o objetivo exibir a pagina dos resultados das buscas.
    """
    campo_busca = request.form["txtBusca"]

    print(f"campo pesquisar: {campo_busca}")
    retorno_vagas = buscador.motor_busca(campo_busca)
    # return render_template('resultado.html',resultado = retorno_vagas)
    return retorno_vagas


@app.route("/login")
def login():
    """
    Essa função tem o objetivo exibir a pagina de login.
    """
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
