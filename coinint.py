#IMPORTAÇÕES E DEFINIÇÕES NECESSARIAS DO SISTEMA

import requests
import json
from bs4 import BeautifulSoup
import subprocess

inicio_artigos = ('/news/') #QUAL URL CONSIDERAR
links_noticias = [] #ALOCAÇÃO DE LINKS DAS NOTICIAS

#URL DE VARREDURA 
urls = [
    'https://cointelegraph.com/'
]

#TODAS AS CLASSES UTILIZADAS PARA A BUSCA DO WEB SCRAPING DENTRO DO SITE
all_class = {
    "post-card", 
    'uni-block uni-block_card rounded-lg', 
    'hidden md:block relative', 
    'px-4 lg:px-0 py-4 lg:py-6', 
    'flex shrink-0 flex-grow flex-nowrap basis-full snap-start snap-always mx-1'
}

####

# WEB SCRAPING DA PAGINA PRINCIPAL COM FORMATAÇÂO DE TEXTO
for u in urls:
    pagina =  requests.get(u)
    dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

    for c in all_class:
        todas_noticias = dados_pagina.find_all('div', class_ = c)

        for div in todas_noticias:
            links = div.find_all('a')

            for link in links:
                href = link['href']

                if(href.startswith(inicio_artigos)):
                    if href not in links_noticias:
                        links_noticias.append(href)

# WEB SCRAPING DAS NOTICIAS COM FORMATAÇÃO DE TEXTO
for l in links_noticias:
    pagina1 = requests.get('https://cointelegraph.com' + l)
    dados_pagina1 = BeautifulSoup(pagina1.text, 'html.parser')

    textos_artigo = []

    corpo_do_texto = dados_pagina1.find('div', class_="post post-page__article")

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

# INICIALIZAÇÃO DO SCRIPT GEMINI.PY PARA GERAR A ANALISE
subprocess.run(["python", "gemini.py"])