from time import strftime, gmtime
from bs4 import BeautifulSoup
from pip._vendor import requests

print("Iniciando as buscas... " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("Buscando dados da selic...")
request = requests.get("http://carteirarica.com.br/taxa-selic/")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find_all("span", {"class": "diano"})
for item in element:
    print(item.text )