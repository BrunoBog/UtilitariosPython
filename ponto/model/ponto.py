from datetime import datetime

from pandas._libs.lib import timedelta


class Ponto(object):
    def __init__(self, dia, funcionario=None, batidas=None,
                 h_trabalhadas=None, previsao_saida=None, restante=None):
        self.dia = dia
        self.funcionario = funcionario
        self.batidas = batidas
        self.h_trabalhadas = h_trabalhadas
        self.previsao_saida = previsao_saida
        self.restante = restante

    def hora_parcial(self):
        hora_total = datetime(self.dia.year, self.dia.month, self.dia.day, 8, 0)
        if self.h_trabalhadas is not None:
            print("Você trabalhou " + str(self.h_trabalhadas))
            return hora_total - self.h_trabalhadas

        if self.batidas[0] is not None:
            return hora_total - self.batidas[0]

        return hora_total

    def calcula_tempo_restante(self):
        print("Oi " + self.funcionario)
        tamanho = len(self.batidas)
        hora_total = datetime(self.dia.year, self.dia.month, self.dia.day, 8, 0)
        if self.h_trabalhadas is not None:
            print("Você trabalhou " + str(self.h_trabalhadas))
            if self.h_trabalhadas >= hora_total:
                self.restante = 0
                self.previsao_saida = 0
                return self.restante
        else:
            if tamanho == 2:
                self.h_trabalhadas = self.batidas[1] - self.batidas[0]
                print("Você trabalhou :" + str(self.h_trabalhadas))
            if tamanho == 3:
                batida1 = self.batidas[1] - self.batidas[0]
                falta_trabalhar = hora_total - batida1
                self.previsao_saida = self.batidas[2] + timedelta(minutes=falta_trabalhar.minute, hours=falta_trabalhar.hour)

            if tamanho == 4:
                batida1 = self.batidas[1] - self.batidas[0]
                batida2 = (self.batidas[3] - self.batidas[2]) + batida1
                if batida2 <= hora_total:
                    self.h_trabalhadas = hora_total - batida2
                else:
                    self.h_trabalhadas = batida2 - hora_total
            if tamanho == 5:
                batida1 = self.batidas[1] - self.batidas[0]
                batida2 = (self.batidas[3] - self.batidas[2]) + batida1

                return hora_total - batida2

    def hora_restante(self):
        tamanho = len(self.batidas)
        hora_total = datetime(self.dia.year, self.dia.month, self.dia.day, 8, 0)
        if self.h_trabalhadas is not None:
            if self.h_trabalhadas > hora_total:
                self.restante = 0
                return self.restante
        else:
            if tamanho == 2:
                self.h_trabalhadas = self.batidas[1] - self.batidas[0]
                self.restante = hora_total - self.h_trabalhadas
                return self.restante
            if tamanho == 3:
                batida1 = self.batidas[1] - self.batidas[0]
                self.restante = hora_total - batida1
                return self.restante 
            if tamanho == 4:
                batida1 = self.batidas[1] - self.batidas[0]
                batida2 = (self.batidas[3] - self.batidas[2]) + batida1
                if batida2 <= hora_total:
                    self.h_trabalhadas = hora_total - batida2
                else:
                    self.h_trabalhadas = batida2 - hora_total
            if tamanho == 5:
                batida1 = self.batidas[1] - self.batidas[0]
                batida2 = (self.batidas[3] - self.batidas[2]) + batida1

                return hora_total - batida2

