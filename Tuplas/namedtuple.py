from collections import namedtuple

Carro = namedtuple('Car', 'cor placa valor')

# Our new "Car" class works as expected:
meu_carro = Carro('vermelho', 'AMC 5586', 35812.4)
print(meu_carro.cor)
print(meu_carro.placa)
print(meu_carro.valor)


# Outro modo para instanciar:
carro_novo = Carro(cor='vermelho' , placa='AGE 5536', valor=40000.66)
print(meu_carro)
print(carro_novo)

# Como Tuplas as namedtubles não podem ter o valor alterado:
#carro_novo.cor= 'azul'
