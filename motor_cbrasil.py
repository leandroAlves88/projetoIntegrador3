import requests
from bs4 import BeautifulSoup

"""
    ConcursosNoBrasil web scrapper and API
"""

URL = "https://concursosnobrasil.com/concursos/"
CABECALHO = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def init_webscraper(url: str, parser: str = "html.parser"):
    """Esse metodo realiza o webscraping na plataforma Concursos do Brasil"""
    try:
        response = ""
        response = requests.get(url, headers=CABECALHO, timeout=20)
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
        return "Site indisponível tente novamente mais tarde"
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")
        return "Erro tente novamente mais tarde"

    if response is None:
        print("Canceling scrapping")
        return None

    return BeautifulSoup(response.content, parser)


def get_status_item(item) -> str:
    """Metodo que valida se a vaga está aberta"""
    try:
        item.find("span", class_="label-previsto").text
    except:
        return "open"

    return "expected"


def concursos_cbrasil(x):
    """Esse metodo realiza a busca de vadas na plataforma Concursos do Brasil"""
    concursos_disponiveis = []
    page_scraper = init_webscraper(URL + x)

    items_retorno = (
        page_scraper.find("main", class_="taxonomy").find("tbody").find_all("tr")
    )  # type: ignore

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
