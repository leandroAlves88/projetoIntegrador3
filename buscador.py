import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy
import re

municipios_cisoeste = [
    "Araçariguama",
    "Barueri",
    "Cajamar",
    "Carapicuiba",
    "Cotia",
    "Itapevi",
    "Jandira",
    "Osasco",
    "Pirapora do Bom Jesus",
    "Santana de Parnaíba",
    "São Roque",
    "Vargem Grande Paulista",
]

# Type of information
nome = []
vagas = []
nivel = []
salario = []
inscricao = []
link = []
combinacao_concursos = []

cabecalho = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
URL1 = "https://www.pciconcursos.com.br/pesquisa/?q="
URL2 = "https://jcconcursos.com.br/busca?q="
URL3 = "https://concursosnobrasil.com/busca/?q="


def motor_busca(campo_pesquisa):
    """
    Descrição da função.

    Essa função tem o objetivo de realizar o processo
    webscraping nas urls de busca.

    :param campo_pesquisa: Esse parametro campo de
    pesquisa recebe o valor do campo digitado no front
    hmtl para iniciar o processo de busca no motor.

    """
    try:
        site = requests.get(URL1 + campo_pesquisa, headers=cabecalho, timeout=20)
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")

    if site != "null" and site is not None:
        print("Retorno: 200")
        soup = site.content

    soup = BeautifulSoup(site.content, "html.parser")
    vaga = soup.find("div", attrs={"id": "concursos"})

    combinacao_concursos = indexacao(soup, "pciconcurso")
    # html_vagas = vaga.find("div", attrs={"class": "ca"})
    # print(vaga.prettify())

    # gravalog(vaga)

    return combinacao_concursos


def gravalog(retorno):
    """
    Descrição da função.

    Essa função tem o objetivo gravar o log do retorno do request.

    :param x: é o objeto que recebeu o retorno do request.

    """
    with open(r"C:\Projetos_Python\log.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(retorno.prettify())


def indexacao(soup, origem):
    """
    Descrição da função.
    Função responsável pela criação da tabela para indexação
    da estrutura do site.
    """
    if origem == "pciconcurso":
        for line in soup.findAll(class_="ca"):
            nome.append(line.find("a").text.strip())  # Institution's name
            link.append(line.find("a", href=True)["href"])  # Link
            vagas.append(
                "".join(re.findall("(\d*) vaga", str(line.find(class_="cd"))))
            )  # Jobs
            nivel.append(
                "/".join(re.findall("Superior|Médio", str(line.find(class_="cd"))))
            )  # Education
            salario.append(
                "".join(re.findall("R\$ *\d*\.*\d*\,*\d*", str(line.find(class_="cd"))))
            )  # Salary
            inscricao.append(
                "".join(re.findall("\d+/\d+/\d+", str(line.find(class_="ce"))))
            )  # Subscription date

        dataframe = pd.DataFrame(nome, columns=["Nome"])
        dataframe["Link"] = link
        dataframe["Vagas"] = vagas
        dataframe["Nivel"] = nivel
        dataframe["Salario"] = salario
        dataframe["Inscrição até"] = inscricao
        dataframe["Origem"] = origem
    # dataframe.to_csv(r"C:\Projetos_Python\your_name.csv")

    return dataframe
