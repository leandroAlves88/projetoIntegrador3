from flask import Flask, render_template, request, redirect, jsonify
import buscador
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    """
    Essa função tem o objetivo de iniciar chamando a pagina princial.
    """
    return render_template("home.html")


@app.route("/resultadoBusca/<campo_busca>", methods=["GET"])
def resultados_busca(campo_busca):
    """Essa função tem o objetivo exibir a pagina dos resultados das buscas."""

    print(f"campo pesquisar: {campo_busca}")
    retorno_vagas = buscador.get_concursos_pci(campo_busca)
    print(retorno_vagas)
    return jsonify(retorno_vagas)


@app.route("/resultados")
def resultados():
    """Rota para a pagina de resultados"""
    return render_template("/resultados.html")


@app.route("/login")
def login():
    """
    Essa função tem o objetivo exibir a pagina de login.
    """
    # campo_login = request.form["txtUsuario"]
    # campo_senha = request.form["txtSenha"]
    # print(campo_login)
    # print(campo_senha)
    return render_template("/login.html")


@app.route("/sobre")
def sobre():
    """
    Essa função tem o objetivo exibir a pagina de login.
    """
    return render_template("sobre.html")


@app.route("/cadastro")
def cadastro():
    """
    Essa função tem o objetivo exibir a pagina de login.
    """
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)  # <-- Modo Debug
