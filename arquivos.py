import os
import sys


def ler_arquivo(path):
    if not os.path.exists(path):
        print("arquivo {} nao existe".format(path))
        sys.exit(-1)
    else:
        _file = open(path, "r")
        data = _file.readlines()
        _file.close()
    return data


def busca_na_lista(lista, search):
    resultado =""
    for line in lista:
        if search in line:
            resultado += line
    return resultado


def read_meta_data(diretorio):
    data = open(diretorio,"r")
    meta_data=[]
    for line in data:
        line_data = line.split('\t')
        meta_data.append((line_data[0],line_data[1],line_data[2]))
    data.close
    return meta_data


def grava_saida(resultado, arquivoSaida):
    saida = ler_arquivo(arquivoSaida)
    saida.append(resultado)
    arquivo = open(arquivoSaida)
    arquivo.writelines(saida)
    arquivo.close()


def lista_conteudo(diretorio):
    todosArquivos = os.listdir(diretorio)