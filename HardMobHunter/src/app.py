import requests
import time
from time import gmtime, strftime
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

print("Procurando Itens no HardMob...")
# caminhoIMG = "C:/Users/BOG/PycharmProjects/HardMobHunter/img/icons8-Bilhete Desconto-64.ico"
while True:
    request = requests.get("http://www.hardmob.com.br/promocoes/")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find_all("a", {"class": "title"})
    toaster = ToastNotifier()
    for item in element:
        if "JBL" in item.text or "Monitor" in item.text or "Cadeira" in item.text:
            print("Encontrei o tópico : " + (item.text.replace("\t", "")).replace("\n", ""))
            print(item.attrs['href'])
            toaster.show_toast("Achei!", item.text, duration=10)

    print("Busca no promobit")
    request = requests.get("https://www.promobit.com.br/")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find_all("a", {"itemprop": "name", "class": "access_url "})
    toaster = ToastNotifier()
    for item in element:
        if "JBL" in item.text or "Monitor" in item.text or "Cadeira" in item.text:
            print("Encontrei o tópico : " + (item.text.replace("\t", "")).replace("\n", ""))
            print("https://www.promobit.com.br/" + item.attrs['href'])
            toaster.show_toast("Achei!", item.text, duration=10)

    print("Busca no Pelando")
    request = requests.get("https://www.pelando.com.br/")
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find_all("a", {"itemprop": "name", "class": "cept-tt linkPlain space--r-1 space--v-1 "})
    toaster = ToastNotifier()
    for item in element:
        if "JBL" in item.text or "Monitor" in item.text or "Cadeira" in item.text:
            print("Encontrei o tópico : " + (item.text.replace("\t", "")).replace("\n", ""))
            print("https://www.pelando.com.br/" + item.attrs['href'])
            toaster.show_toast("Achei!", item.text, duration=10)
            #toaster.show_toast("Achei!", item.text, icon_path=caminhoIMG, duration=10)

    print("Executado em:" + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    time.sleep(60*2)
