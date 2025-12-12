#IMPORTAÇÕES E DEFINIÇÕES NECESSARIAS DO SISTEMA

import requests
import json
from bs4 import BeautifulSoup
import subprocess

inicio_artigos = ('/daybook-us/2025/', '/markets/2025/') #QUAIS URLS CONSIDERAR
links_noticias = [] #ALOCAÇÃO DE LINKS DAS NOTICIAS

#URLS DE VARREDURA 
urls = [
    'https://www.coindesk.com/tag/bitcoin?_gl=1*1ry0zs9*_up*MQ..*_ga*MTA3ODY5MzQxLjE3NjQ4OTk0Njc.*_ga_VM3STRYVN8*czE3NjQ4OTk0NjckbzEkZzAkdDE3NjQ5MDM0ODckajYwJGwwJGg5NzI5MzExMA..',
    'https://www.coindesk.com/tag/ethereum?_gl=1*1ry0zs9*_up*MQ..*_ga*MTA3ODY5MzQxLjE3NjQ4OTk0Njc.*_ga_VM3STRYVN8*czE3NjQ4OTk0NjckbzEkZzAkdDE3NjQ4OTk0NjckajYwJGwwJGg4NzE3NzYwNjk.',
    'https://www.coindesk.com/tag/xrp?_gl=1*1ry0zs9*_up*MQ..*_ga*MTA3ODY5MzQxLjE3NjQ4OTk0Njc.*_ga_VM3STRYVN8*czE3NjQ4OTk0NjckbzEkZzAkdDE3NjQ4OTk0NjckajYwJGwwJGg4NzE3NzYwNjk.'
    'https://www.coindesk.com/tag/solana?_gl=1*1ry0zs9*_up*MQ..*_ga*MTA3ODY5MzQxLjE3NjQ4OTk0Njc.*_ga_VM3STRYVN8*czE3NjQ4OTk0NjckbzEkZzAkdDE3NjQ4OTk0NjckajYwJGwwJGg4NzE3NzYwNjk.'
]

####

# WEB SCRAPING DA PAGINA PRINCIPAL COM FORMATAÇÂO DE TEXTO
for u in urls:
    pagina =  requests.get(u)
    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    todas_noticias = dados_pagina.find_all('div', class_ = "flex flex-col")

    for div in todas_noticias:
        links = div.find_all('a')

        for link in links:
            href = link['href']

            if(href.startswith(inicio_artigos)):
                links_noticias.append(href)

# WEB SCRAPING DAS NOTICIAS COM FORMATAÇÃO DE TEXTO
for l in links_noticias:
    pagina1 = requests.get('https://www.coindesk.com' + l)
    dados_pagina1 = BeautifulSoup(pagina1.text, 'html.parser')

    textos_artigo = []

    corpo_do_texto = dados_pagina1.find('div', class_="document-body font-body-lg")

    if corpo_do_texto:
        paragrafos = corpo_do_texto.find_all('p')
        for elemento in paragrafos:
            textos_artigo.append(elemento.get_text())
        
        titulos1 = corpo_do_texto.find_all('h1')
        for elemento in titulos1:
            textos_artigo.append(elemento.get_text())
            
        titulos2 = corpo_do_texto.find_all('h2')
        for elemento in titulos2:
            textos_artigo.append(elemento.get_text())

        titulos3 = corpo_do_texto.find_all('h3')
        for elemento in titulos3:
            textos_artigo.append(elemento.get_text())

    #CRIAÇÃO/GRAVAÇÃO EM ARQUIVO .JSON  
    try:
        with open("news.json", "r") as file:
            dados_existentes = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        dados_existentes = []

    dados_existentes.append(textos_artigo) 

    news_json = json.dumps(dados_existentes, indent=2)
    with open("news.json", "w") as file:
        file.write(news_json)

# INICIALIZAÇÃO DO SCRIPT COININT.PY PARA FAZER WEBSCRAPING DE OUTRO SITE
subprocess.run(["python", "coinint.py"])
     