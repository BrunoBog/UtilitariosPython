import configparser
import json
from datetime import datetime
from pynubank import Nubank
from NUBank.src.model.Compra import Despesa
from flask import Flask, render_template

app = Flask(__name__)
config = configparser.ConfigParser()
config.read_file(open('config.ini'))
nu = Nubank(config['DEFAULT']['usuario'], config['DEFAULT']['senha'])
dia_fechamento = int(config['DEFAULT']['dia_do_fechamento'])

def add_desp(n):
    desp = Despesa(
        descricao=n['description'],
        categoria=n['category'],
        valor=n['amount'],
        data=datetime.strptime(n['time'], "%Y-%m-%dT%H:%M:%SZ"),
        titulo=n['title'],
        detalhes=n['details'],
        id=n['id'],
        _links=n['_links'],
        link=n['href'],
    )
    return desp


def grava_saida(resultado, arquivoSaida):
    arquivo = open(arquivoSaida, "w")
    arquivo.writelines(resultado)
    arquivo.close()


@app.route("/listarCompras")
def busca_valores():
    # Lista de dicionários contendo todos os eventos do  Nubank (Compras, aumento de limite, pagamentos,etc)
    transactions = nu.get_account_statements()
    despesa = {}
    despesas = {}
    i =0
    for n in transactions:
        data_despesa = datetime.strptime(n['time'], "%Y-%m-%dT%H:%M:%SZ")
        hoje = datetime.now()

        # Após o fechamento do mês anterior
        if data_despesa.year == hoje.year and  data_despesa.month == hoje.month-1 and data_despesa.day > dia_fechamento:
            despesas.update({i: add_desp(n).json()})

        # Despesas do mês corrente
        if data_despesa.year == hoje.year and data_despesa.month == hoje.month and data_despesa.day <= dia_fechamento:
            despesas.update({i: add_desp(n).json()})

        # no caso do mês de dezembro...
        if data_despesa.year == hoje.year-1 and data_despesa.month == 12 and data_despesa.day > dia_fechamento:
            despesas.update({i: add_desp(n).json()})

        i = i+1

    return json.dumps(despesas)


@app.route("/teste")
def teste():
    lista = busca_valores()
    # testando saida em jSon
    grava_saida(json.dumps(lista), 'C:\\Users\\BOG\Desktop\\saida.json')

    soma = 0
    for n in lista.values():
        soma += int(n['valor'])
        print(n['data'], n['descricao'], n['valor'])
    print("total = " + str(soma/100))

    return "total = " + str(soma/100)


if __name__ == '__main__':
    app.run(debug=True)

