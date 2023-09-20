import requests
from bs4 import BeautifulSoup

def motor_busca(campo_pesquisa):    
  cabecalho = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
  url = 'https://www.pciconcursos.com.br/pesquisa/?q='+ campo_pesquisa

  site = requests.get(url, headers=cabecalho)
  soup = site.content

#print(soup)
#print(soup.prettify())

  soup = BeautifulSoup(site.content,'html.parser')
  vaga = soup.find("div", attrs = { "id":"concursos" })

  link = vaga.find_all('a')
  for linkvagas in link:
      print(linkvagas.get('href'))

  descricao = vaga.find_all('a')
  # Imprima os links encontrados
  for tituloVaga in descricao:
      print(tituloVaga.get('title'))

  imagens = vaga.find_all('img')
  # Imprima os links encontrados
  for imagensPrefeituras in imagens:
      print(imagensPrefeituras.get('data-src'))
  
  return ''