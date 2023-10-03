from flask import Flask, render_template, request, redirect
import buscador
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    """
    Essa função tem o objetivo de iniciar chamando a pagina princial.
    """
    return render_template("home.html")


@app.route("/resultadoBusca", methods=["POST"])
def resultadosBusca():
    """
    Essa função tem o objetivo exibir a pagina dos resultados das buscas.
    """
    campo_busca = request.form["txtBusca"]

    print(f"campo pesquisar: {campo_busca}")
    retorno_vagas = buscador.motor_busca(campo_busca)
    retorno_vagas = retorno_vagas.to_html(header="true", index=False, justify="center")
    # return render_template('resultado.html',resultado = retorno_vagas)
    return render_template("resultado.html", df_html=retorno_vagas, title="Vagas")


@app.route("/resultado")
def resultados():
    return render_template("resultado.html")


@app.route("/login")
def login():
    """
    Essa função tem o objetivo exibir a pagina de login.
    """
    # campo_login = request.form["txtUsuario"]
    # campo_senha = request.form["txtSenha"]
    # print(campo_login)
    # print(campo_senha)
    return render_template("login.html")


@app.route("/sobre")
def sobre():
    """
    Essa função tem o objetivo exibir a pagina de login.
    """
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)
