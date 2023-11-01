import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy
import re
from datetime import date
import time

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


CABECALHO = {
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
        site = ""
        site = requests.get(URL1 + campo_pesquisa, headers=CABECALHO, timeout=20)
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")

    if site != "null" and site is not None:
        print("Retorno: 200")
        soup = site.content

    soup = BeautifulSoup(site.content, "html.parser")
    vaga = soup.find("div", attrs={"id": "concursos"})
    combinacao_concursos = pd.DataFrame()
    if len(combinacao_concursos.index) > 0:
        combinacao_concursos.drop()

    combinacao_concursos = indexacao(soup, "pciconcurso")
    # html_vagas = vaga.find("div", attrs={"class": "ca"})
    # print(vaga.prettify())
    # ranqueado = raqueamento(combinacao_concursos)
    gravalog(vaga)

    # return ranqueado
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

        dataframe = pd.DataFrame()
        print("Inicio Indexacao qtd registro dataframe", len(dataframe.index))
        dataframe["Instituição"] = nome
        dataframe["Link"] = link
        dataframe["Vagas"] = vagas
        dataframe["Nivel"] = nivel
        dataframe["Salario"] = salario
        dataframe["Inscrição"] = inscricao
        dataframe["Origem"] = origem

        print("Fim Indexacao qtd registro dataframe", len(dataframe.index))
        # dataframe["Check"] = '<input type="checkbox" id="check" name="check" />'
    # dataframe.to_csv(r"C:\Projetos_Python\your_name.csv")

    return dataframe


def raqueamento(dataframe):
    """Responsável por filtrar o dataframe e trazer as melhores respostas"""
    data = date.today()
    data_formatada = data.strftime("%d/%m/%Y")

    dataframe["Inscrição"] = pd.to_datetime(dataframe["Inscrição"])
    dataframe = dataframe.query(f"'Inscrição' >= {str(data_formatada)}")

    return dataframe


def filtro_concurso_valido(data):
    # print("Informação da data: " + data)
    if data is None or data == "":
        return True
    else:
        data_atual_texto = time.strftime("%d/%m/%Y", time.localtime())
        dia_atual, mes_atual, ano_atual = data_atual_texto.split("/")
        dia, mes, ano = data.split("/")
        ano_igual_ou_maior = int(ano) >= int(ano_atual)
        data_prox_mes_e_valida = ano_igual_ou_maior and int(mes) > int(mes_atual)
        data_mes_atual_e_valida = (
            ano_igual_ou_maior
            and int(mes) == int(mes_atual)
            and int(dia) >= int(dia_atual)
        )
        if data_prox_mes_e_valida or data_mes_atual_e_valida:
            return True
        return False


def get_data_pci(d):
    data_quebrada = d.find("div", {"class": "ce"}).br
    if data_quebrada is not None:
        data = data_quebrada.text
    else:
        data = d.find("div", {"class": "ce"}).text
    return data


def get_json_data(d):
    data = {
        "link": d.a["href"],
        "titulo": d.a.text,
        "data_limite": d.find_all("span")[-1].text,
        "nivel": d.find_all("span")[-2].text,
        "cargo": d.find_all("span")[-3].text,
    }
    return data


def get_concursos_pci(x):
    try:
        response = ""
        response = requests.get(URL1 + x, headers=CABECALHO, timeout=20)
        if response != "null" and response is not None:
            print("Retorno: 200")
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
        return "Site indisponível tente novamente mais tarde"
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")
        return "Erro tente novamente mais tarde"

    # response = requests.get("https://www.pciconcursos.com.br/pesquisa/?q=" + x)
    texto = response.text
    soup = BeautifulSoup(texto, "html.parser")
    concursos = soup.find_all("div", {"class": "ca"})
    concursos_sp = [c for c in concursos if "SP" in c.text]
    # concursos_sp_medio = [c for c in concursos_sp if "Superior" in c.span.text]
    concursos_sp_medio_validos = [
        c for c in concursos_sp if filtro_concurso_valido(get_data_pci(c))
    ]
    concursos_jsonificados = [get_json_data(c) for c in concursos_sp_medio_validos]
    return concursos_jsonificados
