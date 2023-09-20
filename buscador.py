import requests
from bs4 import BeautifulSoup

def motor_busca(campo_pesquisa):    
  cabecalho = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
  url = 'https://www.pciconcursos.com.br/pesquisa/?q='

  site = requests.get(url+campo_pesquisa, headers=cabecalho)
  soup = site.content

  soup = BeautifulSoup(site.content,'html.parser')
  vaga = soup.find("div", attrs = { "id":"concursos" })
  
  htmlVagas = vaga.find('div', attrs = {'class':'ca'})
  print(htmlVagas.prettify())
  
  return vaga.prettify()