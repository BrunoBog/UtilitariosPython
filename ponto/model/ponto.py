from datetime import datetime

from pandas._libs.lib import timedelta

from ponto.common.mongo import Database


class Ponto(object):
    collection = 'ponto'

    def __init__(self, dia, funcionario=None, batidas=None,
                 h_trabalhadas=None, previsao_saida=None, restante=None):
        self.dia = dia
        self.funcionario = funcionario
        self.batidas = batidas
        self.h_trabalhadas = h_trabalhadas
        self.previsao_saida = previsao_saida
        self.restante = restante
        self.hora_total = datetime(self.dia.year, self.dia.month, self.dia.day, 8, 0)

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
                return self.restante
        else:
            if tamanho == 1:
                self.h_trabalhadas = datetime.now() - self.batidas[0]
                self.restante = timedelta(hours=8) - self.h_trabalhadas
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
        if self.h_trabalhadas is not None:
            if len(self.batidas) != 2:
                if (self.hora_total - self.h_trabalhadas).hour > 8:  #comentei um
                    self.restante = 0
                    return self.restante
            else:
                self.restante = self.hora_total - self.h_trabalhadas
                return self.restante

        else:
            self.calcula_restante()

    def calcula_restante(self):
        tamanho = len(self.batidas)
        if tamanho == 2:
            self.h_trabalhadas = self.batidas[1] - self.batidas[0]
            self.restante = self.hora_total - self.h_trabalhadas
            return self.restante
        if tamanho == 3:
            batida1 = self.batidas[1] - self.batidas[0]
            self.restante = self.hora_total - batida1
            return self.restante
        if tamanho == 4:
            batida1 = self.batidas[1] - self.batidas[0]
            batida2 = (self.batidas[3] - self.batidas[2]) + batida1
            if batida2 <= self.hora_total:
                self.h_trabalhadas = self.hora_total - batida2
            else:
                self.h_trabalhadas = batida2 - self.hora_total
        if tamanho == 5:
            batida1 = self.batidas[1] - self.batidas[0]
            batida2 = (self.batidas[3] - self.batidas[2]) + batida1
            return self.hora_total - batida2

    def insere_batida(self):
        pass

    def busca_ponto(self):
        Database.find_one(collection=self.collection, query='dia=self.dia')

    def json(self):
        return {
            "dia": self.dia,
            "funcionario": self.funcionario,
            "batidas": self.batidas,
            "h_trabalhadas": self.h_trabalhadas,
            "previsao_saida": self.previsao_saida,
            "restante": self.restante,
            "hora_total": self.hora_total
        }