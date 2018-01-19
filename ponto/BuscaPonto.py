import configparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import request
from flask.app import Flask
from flask.templating import render_template

from ponto.common.mongo import Database
from ponto.model.ponto import Ponto

config = configparser.ConfigParser()
config.read_file(open( 'config.ini' ))

app = Flask(__name__)
app.secret_key = 'superSecretA'


def buscar_ponto(login=None, password=None):
    login = login if login is not None else config['DEFAULT']['usuario']
    password = password if password is not None else config['DEFAULT']['senha']
    s = requests.session()
    auth = {
        "username": login
        ,'passwd': password
        ,'option': 'login'
        ,"lang": "brazilian_portuguese"
        ,"message": "0"
        ,"force_session": "1"
        ,"j0186c0bd9433da88fa21fa7c7bf34ae7": "1"
        ,'op2': 'login'
        ,"Submit": 'Submit'
    }

    s.post('https://portal.seniorsolution.com.br/portal/index.php', data=auth)

    response = s.get('https://portal.seniorsolution.com.br/portal/portal.php/rh/ponto/browse')
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find_all("td", {"nowrap": "nowrap"})

    if element is None or len(element) <=0:
        return

    ponto = preenche_ponto(element=element)

    return ponto


def preenche_ponto(element):
    # Extraindo o dia
    dia = element[0].text.split("/")
    ano=dia[2].strip().split(" ")
    data = datetime.strptime(dia[0].strip() + "/"+dia[1].strip() + "/"+ano[0], '%d/%m/%Y')
    ponto = Ponto(dia=data)

    # Extraindo o Nome do funcionario
    ponto.funcionario = element[1].text.strip()

    # agora as batidas
    lista = []
    for n in range(len(element)):
        if n > 1:
            if element[n].text.strip() != '':
                hora = datetime.strptime(element[n].text.strip(), '%H:%M')
                batida = datetime(data.year, data.month, data.day, hora.hour, hora.minute)
                if n <= 7:
                    lista.append(batida)
                    continue

            if n == 10:
                if element[n].text.strip() != '':
                    ponto.h_trabalhadas = batida
            else:
                continue
    ponto.batidas = lista

    if ponto.h_trabalhadas is None:
        ponto.calcula_tempo_restante()

    return ponto

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route("/exibePonto", methods=['POST'])
def exibe_ponto():
    login = request.form.get('login')
    password = request.form.get('password')
    ponto = buscar_ponto(login=login, password=password)
    if ponto is not None:
        ponto.hora_restante()
        return render_template("lista_ponto.html", ponto=ponto, restante=ponto.restante)

    return "<h1>Não foi possível buscar seu ponto</h1>"


if __name__ == '__main__':
    app.run(port=4992, debug=True, host='0.0.0.0')