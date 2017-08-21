import pymongo
# modulo = __import__("MeuModulo.py")
# variável = getattr(MeuModulo, "soma")

url = "mongodb://127.0.0.1:27017"

cliente = pymongo.MongoClient(url)

database = cliente["fullstack"]
collection = database["students"]

# deste modo students vira uma lista e não preciso faz\er o for como abaixo
students = [student['email'] for student in collection.find({}) if student['email'] == 'abacates@gmail.com']
print(students)

#modo + simples...
# students = collection.find({})
# for student in students :
#     print(student)

cliente.close()