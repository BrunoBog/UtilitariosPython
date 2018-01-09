import configparser

from datetime import datetime
from pynubank import Nubank
import pandas as pd

from NUBank.src.model.Compra import Despesa

config = configparser.ConfigParser()
config.read_file(open('config.ini'))

nu = Nubank(config['DEFAULT']['usuario'],config['DEFAULT']['senha'])

# Lista de dicionários contendo todos os eventos do seu Nubank (Compras, aumento de limite, pagamentos,etc)
transactions = nu.get_account_statements()
lista = []
for n in transactions:

    lista.append(Despesa(
        descricao=n['description'],
        categoria=n['category'],
        valor=n['amount'],
        data=datetime.strptime(n['time'], "%Y-%m-%dT%H:%M:%SZ"),
        titulo=n['title'],
        detalhes=n['details'],
        letitude=n['lat'],
        longitude=n['lon'],
        subcategoria =n['subcategory'],
        id=n['id'],
        _links=n['_links'],
        link=n['href'],
        ))

# # Soma de todas as compras
# sum([t['amount'] for t in transactions])
#
# df = pd.DataFrame(transactions, columns=['time', 'description', 'amount'], )
# df['time'] = pd.to_datetime(df['time'])
# resp = df.groupby([df.time.dt.year, df.time.dt.month, df.time.dt.day,  df.description]).sum() # Agrupado por Ano/Mês
# # df.to_csv('C:\\Users\\bruno.alves\\Desktop\\mine\\fatura.csv', sep='\t', encoding='utf-8')
# print(resp)