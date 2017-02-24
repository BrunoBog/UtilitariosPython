#coding: utf-8
import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Download %d" %(((time * BUFF_SIZE) /length)*100))
		
		
def download(response, output):
    total.download = 0
    while true:
        data = response.read(buff_size)
        total.download += len(data)
        if not data:
            break
        out_file.write(data)
        print("Download {bytes}".format(bytes = total_downloaded))

def main():
    if len(sys.argv) >1:
        response = request.urlopen(sys.argv[1])
    else:
        response = request.urlopen("http://livropython.com.br/dados.zip")
    out_file = io.FileIO("saida.zip",mode = "w")

    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response,out_file)
    
    response.close()
    out_file.close()
    print("Acabou")
	
if __name__ == "__main__":
    main()
    	
  	
