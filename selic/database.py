import pyrebase


class firebase(object):
    user = None
    config = {
        "apiKey": "AIzaSyB7_2SlMHnnXx96vDcVjY9CFMdsLUEnv3I",
        "authDomain": "financaspessoais-45f54.firebaseapp.com",
        "databaseURL": "https://financaspessoais-45f54.firebaseio.com",
        "storageBucket": "financaspessoais-45f54.appspot.com",
        "serviceAccount": "C:\\Users\\BOG\\OneDrive\\Documentos\\Financas-b85e1f6526a1.json"
    }

    def __init__(self):
        self.firebase = pyrebase.initialize_app(self.config)

    def auth(self, email, senha):
        auth = firebase.auth()
        # authenticate a user
        self.user = auth.sign_in_with_email_and_password(email, senha)

    @staticmethod
    def inserirFirebase(data, collection, user):
        return firebase.child(collection).push(data, user['idToken'])

    @staticmethod
    def buscarGeral(collection, user):
        return firebase.child(collection).get(user['idToken']).val()

    @staticmethod
    def busca_um(collection, user, termo):
        return firebase.child(collection).child(termo).get(user['idToken']).val()

    @staticmethod
    def aterar(collection, user, termo):
        firebase.child("agents").child("Lana").update({"name": "Lana Anthony Kane"}, user['idToken'])
        firebase.child(collection).child("Morty").update({"name": "Mortiest Morty"})

    @staticmethod
    def apagarTodos(collection, user):
        firebase.child(collection).remove(user['idToken'])

    @staticmethod
    def apagaUm(collection, user, termo):
        firebase.child(collection).child(termo).remove(user['idToken'])

    @staticmethod
    def insere(collection, data):  # data in Json
        firebase.child(collection).push(data)
        # ou ....
        # firebase.child(collection).child("subcollection").set(data)1
