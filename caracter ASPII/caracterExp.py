#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re

from Arquivos.arquivos import ler_arquivo

caracterValido = []


def char_valido():
    for x in range(32, 126):
        caracterValido.append(chr(x))
    return caracterValido


def grava_saida(linhas_invalidas):
    arq = open('result.txt','w')
    for n in linhas_invalidas:
        arq.write(n)
    arq.close()


def verifica_invalido(frase, validos):
    for n in frase:
        if n not in validos:
            frase = frase.replace(n, "")

    return frase


def main():
    conteudo = ler_arquivo(r'C:\Users\bruno.alves\exportar.txt')
    caracter_valido = char_valido()
    caracterValido.append('\t')
    caracterValido.append('\n')
    linhas_invalidas=[]

    for x in conteudo:
        linhas_invalidas.append(verifica_invalido(x, caracter_valido))

    grava_saida(linhas_invalidas)





if __name__ == '__main__':
    main()