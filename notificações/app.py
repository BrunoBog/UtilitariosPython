import time

import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


lista=[]
lista.append("615217")


def main():
    toaster = ToastNotifier()
    # hunt(615217)
    while(True):
        for n in lista:
            toaster.show_toast("Lembrete!!!", "Chamado " + str(n), duration=10) #icon_path="custom.ico"
            time.sleep(60 * 5)

def main():
    pass

def hunt(chamado=615217):
    request = requests.get('http://cat/catfrmlogin.aspx?acao=con&fat_codigo=' + str(chamado))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    element = soup.find_all("span", {"id": "lbloco_data_gravacao_0", "class": "labelnormal "})

    print(element)


if __name__ == '__main__':
    hunt()