import requests
from bs4 import BeautifulSoup


def motor_busca(campo_pesquisa):
    """
    Descrição da função.

    Essa função tem o objetivo de realizar o processo
    webscraping nas urls de busca.

    :param campo_pesquisa: Esse parametro campo de
    pesquisa recebe o valor do campo digitado no front
    hmtl para iniciar o processo de busca no motor.

    """

    cabecalho = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    url1 = "https://www.pciconcursos.com.br/pesquisa/?q="

    try:
        site = requests.get(url1 + campo_pesquisa, headers=cabecalho, timeout=20)
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")

    if site != "null" and site is not None:
        soup = site.content

    soup = BeautifulSoup(site.content, "html.parser")
    vaga = soup.find("div", attrs={"id": "concursos"})

    # htmlVagas = vaga.find("div", attrs={"class": "ca"})
    # print(htmlVagas.prettify())

    gravalog(vaga)

    return vaga.prettify()


def gravalog(retorno):
    """
    Descrição da função.

    Essa função tem o objetivo gravar o log do retorno do request.

    :param x: é o objeto que recebeu o retorno do request.

    """
    with open(r"C:\Projetos_Python\log.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(retorno.prettify())
