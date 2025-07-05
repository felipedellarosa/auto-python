#AUTOMATIZAÇÃO DE WEB SCRAPING (Extração de Dados da Web)

from bs4 import BeautifulSoup
import requests

def extrair_informacoes_site():
    url ="https://www.nationalgeographicbrasil.com/historia"
    headers = {"User-Agent": "Mozilla/5.0"}
    requisicao = requests.get(url, headers=headers)

    if requisicao.status_code == 200:
        pagina = BeautifulSoup(requisicao.text, "html.parser")
        titulos = pagina.find_all(class_="css-5trwwb")
        for titulo in titulos:
            print(titulo.text)

extrair_informacoes_site()