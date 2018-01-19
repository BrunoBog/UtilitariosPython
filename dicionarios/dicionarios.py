d1 = {}
d2 = dict()

d1['aaa'] = 1000
print(d1)

d2['ttt'] = 2000
d1['bbb'] = 2000
d1['ccc'] = 3000
print(d1)

print("Procurando um valor:")
print(d1['bbb'])


#checando valores
print(2000 in d1)

print("Usando o pop:")
print(d1.popitem())
print(d1)


# merde dict
d1.update(d2)
print(d1)

# or
d4 = {**d1, **d2}
print("Resultado do d4")
print(d4)