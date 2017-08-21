from time import strftime, gmtime
import requests
from bs4 import BeautifulSoup


class Selic(object):
    def __init__(self, data=None, valor=None):
        self.data = strftime("%Y-%m-%d %H:%M:%S", gmtime()) if data is None else data
        self.valor = 0  # float(self.BuscarValorAtual()) if valor is None else valor

    def buscaValor(self):
        print("Iniciando as buscas... " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        print("Buscando dados da selic...")
        request = requests.get("http://carteirarica.com.br/taxa-selic/")
        content = request.content
        soup = BeautifulSoup(content, "html.parser")
        element = soup.find_all("span", {"class": "diano"})
        self.valor = element[0].text
        self.data = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print(element[0].text)

    def json(self):
        return {
            "dia": self.data,
            "valor": self.valor
        }
