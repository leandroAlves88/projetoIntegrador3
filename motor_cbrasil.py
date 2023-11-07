import requests
from bs4 import BeautifulSoup

"""
    ConcursosNoBrasil web scrapper and API
"""

availableCategories = [
    "br",
    "ac",
    "al",
    "am",
    "ap",
    "ba",
    "ce",
    "df",
    "es",
    "go",
    "ma",
    "mg",
    "ms",
    "mt",
    "pa",
    "pb",
    "pe",
    "pi",
    "pr",
    "rj",
    "rn",
    "ro",
    "rr",
    "rs",
    "sc",
    "se",
    "sp",
    "to",
]
baseURL = "https://concursosnobrasil.com/concursos/"
errorMessage = ""


def pageRequest(url: str):
    try:
        return requests.get(url)
    except requests.HTTPError:
        print("An http error has ocurred, process has exited")
        return None
    except:
        print("An error has ocurred, process has exited")
        return None


def initWebScraper(url: str, parser: str = "html.parser"):
    webResponse = pageRequest(url)

    if webResponse == None:
        print("Canceling scrapping")
        return None

    return BeautifulSoup(webResponse.content, parser)


def categoryTarget(category: str) -> str:
    global errorMessage
    if (len(category) != 2) or (category not in availableCategories):
        errorMessage = "Invalid Category"
        return ""

    return baseURL + category


def getCategoryItemStatus(item) -> str:
    try:
        item.find("span", class_="label-previsto").text
    except:
        return "open"

    return "expected"


def concursos_cbrasil(categorySelect):
    concursosAvailable = []
    pageScraper = initWebScraper(categoryTarget(categorySelect))

    print(pageScraper.prettify())

    with open(
        r"C:\Projetos_Python\concursosnobrasil.html", "w", encoding="utf-8"
    ) as arquivo:
        arquivo.write(pageScraper.prettify())

    availableItemsInCategory = (
        pageScraper.find("main", class_="taxonomy").find("tbody").find_all("tr")
    )  #  type: ignore

    for item in availableItemsInCategory:
        concursosAvailable.append(
            {
                "organization": item.find("a").text.rstrip(),
                "workPlacesAvailable": item.find_all("td")[1].text.rstrip(),
                "link": item.find("a").get("href"),
                "status": getCategoryItemStatus(item),
            }
        )

    # print(concursosAvailable)
    return concursosAvailable
