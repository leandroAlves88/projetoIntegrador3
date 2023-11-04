from flask import Flask, render_template, request, redirect, jsonify
import buscador

app = Flask(__name__)


@app.route("/")
def home():
    """
    Essa função tem o objetivo de iniciar chamando a pagina princial.
    """
    return render_template("home.html")


@app.route("/buscaVagasSP/<campo_busca>", methods=["GET"])
def resultados_busca(campo_busca):
    """Essa função tem o objetivo exibir a pagina dos resultados das buscas."""

    print(f"campo pesquisar: {campo_busca}")
    retorno_vagas = buscador.get_concursos_pci(campo_busca)
    print(retorno_vagas)
    return jsonify(retorno_vagas)


@app.route("/buscaVagas/cioeste", methods=["GET"])
def busca_cisoeste():
    """Essa função tem o objetivo exibir as vagas das cidades pertencentes ao grupo cisoeste."""
    retorno_vagas = buscador.get_concursos_cisoeste()
    print(retorno_vagas)
    return jsonify(retorno_vagas)


@app.route("/buscaVagas/cioeste/<cidade>", methods=["GET"])
def busca_cisoeste_cidade(cidade):
    """Essa função tem o objetivo exibir a pagina dos resultados das buscas."""

    print(f"campo pesquisar: {cidade}")
    retorno_vagas = buscador.get_concursos_cisoeste_cidade(cidade)
    print(retorno_vagas)
    return jsonify(retorno_vagas)


@app.route("/cioeste")
def resultados():
    """Rota para a pagina de busca do grupo de cidades cioeste"""
    return render_template("/cioeste.html")


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
