#coding utf-8
import io
import sys
import os

def read_meta_data(diretorio):
    data = open(diretorio,"r")
    meta_data=[]
    for line in data:
        line_data = line.split('\t')
        meta_data.append((line_data[0],
                          line_data[1],
                          line_data[2]))
    data.close
    return meta_data
    

def main():
    if len(sys.argv)> 1:
        diretorio = sys.argv[1]
    else:
        diretorio = 'C:\\Users\\balves\\Desktop\\python'
         
    for meta_file in os.listdir(diretorio):
        print(meta_file)

    for lista in read_meta_data(diretorio):
        print (lista)


if __name__ == '__main__':
    main()
