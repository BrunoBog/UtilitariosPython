#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

caracterValido = []


def charvalido():
    caracterValido = []
    for x in range(32, 126):
        # print (chr(x))
        caracterValido.append(chr(x))
    return caracterValido


def grava_saida(resultado, arquivoSaida):
    saida = ler_arquivo(arquivoSaida)
    saida.append(resultado)
    arquivo = open(arquivoSaida)
    arquivo.writelines(saida)
    arquivo.close()


def ler_arquivo(path):
    if not os.path.exists(path):
        print("arquivo {} nao existe".format(path))
        sys.exit(-1)
    else:
        _file = open(path, "r", encoding="utf8")
        data = _file.readlines()
        _file.close()
    return data

def main():
    arquivo = (r'C:\Users\bruno.alves\exportar.txt')
    conteudo = ler_arquivo(arquivo)
    caracterValido = charvalido()
    caracterValido.append('\t')
    caracterValido.append('\n')
    linhasInvalidas=[]

    for x in conteudo:
        linhasInvalidas.append(verificaInvalido(x))
    # grava_saida(linhasInvalidas, r'C:\Users\bruno.alves\linhas.txt')

    for n in linhasInvalidas:
        print(n)


def verificaInvalido(frase):
    for n in frase:
        if n not in caracterValido:
            frase.replace(n,"")

    return frase


if __name__ == '__main__':
    main()