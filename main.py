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
def resultadosBusca(campo_busca):
    """
    Essa função tem o objetivo exibir a pagina dos resultados das buscas.
    """
    # campo_busca = request.form["txtBusca"]
    print(f"campo pesquisar: {campo_busca}")
    retorno_vagas = buscador.get_concursos_pci(campo_busca)

    """retorno_vagas = pd.DataFrame()
    print("Quantidade de registros iniciais:", len(retorno_vagas.index))

    retorno_vagas = buscador.motor_busca(campo_busca)
    print(type(retorno_vagas))

    print("Quantidade de registros encontrados:", len(retorno_vagas.index))

    retorno_vagas = retorno_vagas.to_html(header="true", index=False, justify="center")"""

    # return render_template("/resultados.html", df_html=retorno_vagas, title="Vagas")
    print(retorno_vagas)
    return jsonify(retorno_vagas)


@app.route("/resultados")
def resultados():
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
