import requests
from bs4 import BeautifulSoup
import time

municipios_cioeste = [
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


CABECALHO = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
URL1 = "https://www.pciconcursos.com.br/pesquisa/?q="
URL1CISOESTE = "https://www.pciconcursos.com.br/concursos/sudeste/"


def gravalog(retorno):
    """
    Descrição da função.

    Essa função tem o objetivo gravar o log do retorno do request.

    :param x: é o objeto que recebeu o retorno do request.

    """
    with open(r"C:\Projetos_Python\log.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(retorno.prettify())


def filtro_concurso_valido(data):
    """valida se a data do concurso está vencida"""
    try:
        if "Cancelado" in data:
            return False
        elif data is None or data == "":
            return True
        elif "/" not in data:
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
    except:
        return True


def get_data_pci(d):
    """valida o campo data"""
    data_quebrada = d.find("div", {"class": "ce"}).br
    if data_quebrada is not None:
        data = data_quebrada.text
    else:
        data = d.find("div", {"class": "ce"}).text
    return data


def get_json_data(d):
    """Transforma o retorno em dicionario para construção do Json"""
    data = {
        "link": d.a["href"],
        "titulo": d.a.text,
        "data_limite": d.find_all("span")[-1].text,
        "nivel": d.find_all("span")[-2].text,
        "cargo": d.find_all("span")[-3].text,
    }
    return data


def get_concursos_pci(x):
    """Realiza a busca no site pciconsurso e tranforma os dados em json"""
    try:
        response = ""
        response = requests.get(URL1 + x, headers=CABECALHO, timeout=20)
        if response.status_code == 200:
            print("Retorno: 200")
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
        return "Site indisponível tente novamente mais tarde"
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")
        return "Erro tente novamente mais tarde"

    texto = response.text
    soup = BeautifulSoup(texto, "html.parser")
    concursos = soup.find_all("div", {"class": "ca"})
    concursos_sp = [c for c in concursos if "SP" in c.text]
    concursos_sp_validos = [
        c for c in concursos_sp if filtro_concurso_valido(get_data_pci(c))
    ]
    concursos_jsonificados = [get_json_data(c) for c in concursos_sp_validos]
    return concursos_jsonificados


def get_concursos_cisoeste():
    """Realiza a busca no site pciconsurso e tranforma os dados em json"""
    try:
        response = ""
        response = requests.get(URL1CISOESTE, headers=CABECALHO, timeout=20)
        if response.status_code == 200:
            print("Retorno: 200")
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
        return "Site indisponível tente novamente mais tarde"
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")
        return "Erro tente novamente mais tarde"

    texto = response.text
    soup = BeautifulSoup(texto, "html.parser")
    concursos = soup.find_all("div", {"class": "ca"})
    concursos_sp = [c for c in concursos if "SP" in c.text]
    concursos_sp_cisoeste = [
        c for c in concursos_sp if any(word in c.a.text for word in municipios_cioeste)
    ]
    concursos_sp_validos = [
        c for c in concursos_sp_cisoeste if filtro_concurso_valido(get_data_pci(c))
    ]
    concursos_jsonificados = [get_json_data(c) for c in concursos_sp_validos]
    return concursos_jsonificados


def get_concursos_cisoeste_cidade(cidade):
    """Realiza a busca no site pciconsurso e tranforma os dados em json"""
    try:
        response = ""
        response = requests.get(URL1CISOESTE, headers=CABECALHO, timeout=20)
        if response.status_code == 200:
            print("Retorno: 200")
    except requests.Timeout:
        print("A solicitação atingiu o tempo limite de 10 segundos.")
        return "Site indisponível tente novamente mais tarde"
    except requests.RequestException as erro:
        print(f"Ocorreu um erro na solicitação: {erro}")
        return "Erro tente novamente mais tarde"

    texto = response.text
    soup = BeautifulSoup(texto, "html.parser")
    concursos = soup.find_all("div", {"class": "ca"})
    concursos_sp = [c for c in concursos if "SP" in c.text]
    concursos_sp_cisoeste = [c for c in concursos_sp if cidade in c.a.text]
    concursos_sp_validos = [
        c for c in concursos_sp_cisoeste if filtro_concurso_valido(get_data_pci(c))
    ]
    concursos_jsonificados = [get_json_data(c) for c in concursos_sp_validos]
    return concursos_jsonificados
