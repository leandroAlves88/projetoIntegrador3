# projetoIntegrador3
Esse repositório tem como objetivo a entrega do projeto integrador

# Rodar o sistema de forma localhost
Execução local do sistema

- venv/Scripts/activate

- $env:FLASK_APP = "main"

- flask run

# FrontEnd do sistema Super Edital
O sistema Super Edital tem com objetivo facilar a busca por concursos públicos de São Paulo e região.(Não oficial).
Esse projeto faz parte do projeto Integrador 3 da Fatec Santana de Parnaíba.

# Backend do sistema Super Edital
O sistema utiliza um motor de busca desenvolvido em [Python](https://www.python.org/) que coletam os dados de três plataformas de concursos públicos.
As fontes de dados se originam dos sites:
>[PCI Concursos](https://www.pciconcursos.com.br)
>[JC Concursos](https://www.jcconcursos.com.br)
>[Concursos no Brasil](https://www.concursosnobrasil.com)

# Uso
Esse projeto tem caráter educativo e usa dados contidos no website citados anteriormente. Todo conteúdo utilizado é de propriedade e responsabilidade dos mesmos.

Modificações nas estruturas de página nos sites origem podem causar indisponibilidade no sistema, devido a tecnica webScraping utilizada para adquirir dados.

Recomendação: __NÃO USAR EM PRODUÇÃO__.

# Tecnologias
  >[Flask](https://flask.palletsprojects.com/en/3.0.x/) - O Flask é um microframework web projetado para ser simples e fácil de usar, permitindo que os desenvolvedores construam rapidamente aplicativos web e APIs.
  
  >[BeautifulSoup 4](https://pypi.org/project/beautifulsoup4/) - Beautiful Soup é uma biblioteca que facilita a extração de informações de páginas da web.

  >[Requests](https://pypi.org/project/requests/) - É um pacote python que permite enviar solicitações http.
