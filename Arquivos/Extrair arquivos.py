#coding utf-8

import os
import zipfile
import sys

def main(path):
    if not os.path.exists(path):
        print("arquivo {} nao existe".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("arquivo extraido")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('C:\\Users\\Bruno\OneDrive\\Documentos\\Desenvolvimento\\phyton\\Exemplos')