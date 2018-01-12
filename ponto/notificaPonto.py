import time
from pandas._libs.lib import timedelta, datetime
from ponto.BuscaPonto import buscar_ponto
from win10toast import ToastNotifier


def notifica():
    toaster = ToastNotifier()
    ponto = buscar_ponto()
    notifica_almoco = datetime.now()
    notifica_saida = datetime.now()
    ponto.calcula_tempo_restante()
    ponto.hora_restante()

    while True:
        if len(ponto.batidas) == 2:
            if notifica_almoco < notifica_almoco + timedelta(minutes=5):
                notifica_almoco = datetime.now()
                print("Retorno do almoço: " + str(ponto.batidas[3] + timedelta(hours=1)))
                print("Horas trabalhadas / Restante: " + str(ponto.h_trabalhadas.time() + timedelta(hours=1)))

            if len(ponto.batidas) == 2:
                toaster.show_toast("oi!!!",
                                   "Seu retorno do almoço será: " + str((ponto.batidas[1] + timedelta(hours=1)).time()),
                                   duration=10)

        if notifica_saida < (notifica_saida + timedelta(hours=1)):
            notifica_saida = datetime.now()
            if ponto.previsao_saida > 0:
                toaster.show_toast("oi!!!", "Sua previsão de saida: " + str(ponto.previsao_saida.time()), duration=10)

        if ponto.h_trabalhadas.hour >= 8:
            toaster.show_toast("Vá!!!", "Você já completou 8 Horas ", duration=10)


if __name__ == '__main__':
    notifica()