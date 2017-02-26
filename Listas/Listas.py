#Exemplo de listas
# lista = [100,200,300]
# for item in range(len(lista)):
#     lista[item] += 100
# print (lista)

#enumerate
# lista = ['aaa','bbb','ccc']
# lista = list(enumerate(lista))
# print(lista)

#Exemplo em Lista
# lista=[100,200,300]
# for idx, item in enumerate(lista):
#     lista[idx] *= 100
# print(lista)

#imprimir uma lista
lista=[100,200,300]
print(lista)

#iMPRIMIR UMA LISTA DE TRAZ PRA FRENTE
lista=[100,200,300]
print(lista[::-1])

#iMPRIMIR UMA LISTA  ATÉ A POSIÇÃO X
x = 2
lista=[100,200,300]
print(lista[:x])

#inverter os dados de uma lista
lista=[100,200,300]
lista.reverse()
print(lista)
