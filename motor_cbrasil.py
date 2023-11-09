import requests
from bs4 import BeautifulSoup

URL = "https://concursosnobrasil.com/concursos/"
CABECALHO = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def request_pagina(url: str):
    """Esse metodo realiza a requisição a plataforma Concursos do Brasil"""
    try:
        return requests.get(url, headers=CABECALHO, timeout=20)
    except requests.HTTPError:
        print("An http error has ocurred, process has exited")
        return None
    except:
        print("An error has ocurred, process has exited")
        return None


def init_webscraper(url: str, parser: str = "html.parser"):
    """Esse metodo realiza o webscraping na plataforma Concursos do Brasil"""
    response = request_pagina(url)

    if response is None:
        print("Canceling scrapping")
        return None

    return BeautifulSoup(response.content, parser)


def get_status_item(item) -> str:
    """Metodo que valida se a vaga está aberta"""
    if item.find("div", class_="label-previsto") is None:
        print("Retorno -> Aberto")
        return "Aberto"
    else:
        print("Retorno -> Previsto")
        return "Previsto"


def concursos_cbrasil(x):
    """Esse metodo realiza a busca de vadas na plataforma Concursos Brasil"""
    concursos_disponiveis = []
    page_scraper = init_webscraper(URL + x)

    items_retorno = (
        page_scraper.find("main", class_="taxonomy").find("tbody").find_all("tr")
    )
    with open(
        r"C:\Projetos_Python\concursosBrasil.html", "w", encoding="utf-8"
    ) as arquivo:
        arquivo.write(page_scraper.prettify())

    for item in items_retorno:
        concursos_disponiveis.append(
            {
                "organization": item.find("a").text.rstrip(),
                "workPlacesAvailable": item.find_all("td")[1].text.rstrip(),
                "link": item.find("a").get("href"),
                "status": get_status_item(item),
            }
        )

    return concursos_disponiveis
