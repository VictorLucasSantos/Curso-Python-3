"""
+ Web Scraping com Python usando requests e bs4 BeautifulSoup
- Web Scraping é o ato de "raspar a web" buscando informações de forma
automatizada, com determinada linguagem de programação, para uso posterior.
- O módulo requests consegue carregar dados da Internet para dentro do seu
código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
em formato de objetos Python para facilitar a vida do desenvolvedor.
- Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
+ Instalação
- pip install requests types-requests bs4
"""

import requests
import re
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/Secao%2006/aula190_site/index.html"

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, "html.parser")

print(parsed_html.title)
# print(parsed_html)

top_jobs_heading = parsed_html.select_one(" #intro > div > div > article > h2")

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    print(article.text)  # Obtendo todos os dadaos da tag articles Jobs

    if article is not None:
        for p in article.select("p"):
            print(re.sub(r"\s{1,}", " ", p.text).strip())
