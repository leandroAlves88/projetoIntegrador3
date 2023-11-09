import requests
from bs4 import BeautifulSoup

URL_BASE = "https://jcconcursos.com.br/concursos/inscricoes-abertas/"
CABECALHO = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def get_concursos_jcconcursos(x):
    """Realiza a busca no site pciconsurso e tranforma os dados em json"""
    response = ""
    response = requests.get(URL_BASE + x, headers=CABECALHO, timeout=20)
    texto = response.text
    soup = BeautifulSoup(texto, "html.parser")

    concursos = soup.find_all("div", {"class": "row border-bottom py-3"})

    concursos_jsonificados = [get_json_data(c) for c in concursos]

    return concursos_jsonificados


def get_json_data(d):
    """Transforma o retorno em dicionario para construção do Json"""
    data = {
        "link": "https://jcconcursos.com.br" + d.a["href"],
        "titulo": d.h2.text.strip("Previsto"),
        "salario": d.find_all("span")[-2].text.strip("Previsto"),
        "Status": d.find_all("span")[-0].text,
        "Nivel": d.find_all("span")[1].text.strip("Previsto"),
        "numero_vagas": d.find_all("span")[-1].text.strip("Previsto"),
    }
    return data
