from pyrebase import pyrebase
from modules.selic import Selic

# config = {
#         "apiKey": "",
#         "authDomain": "",
#         "databaseURL": "",
#         "storageBucket": "",
#         "serviceAccount": ""
#     }
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# user = auth.sign_in_with_email_and_password('teste@testadormaster.com', 'RootsBloodRoots')
# db = firebase.database()

selic = Selic()
selic.buscaValor()
print(selic.json())

# salvar
# db.child("selic").push(selic.json(),user['idToken'])

# ler todos
# taxa = db.child("selic").get(user['idToken'])
# print(taxa.val())

# ler cada
# taxa = db.child("selic").get(user['idToken'])
# for tx in taxa.each():
#     print(tx.key())
#     print(tx.val())
