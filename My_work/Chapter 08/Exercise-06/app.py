"""Exercise 6
Write a program that displays the file name, size, and modification date for all those files in a directory that are greater than a given size.
The directory name and the size criteria are given as command line arguments."""

import sys
import os
import time   

#terminal exemplo: python app.py ./pastateste 1024 

pasta = sys.argv[1]
valor_tamanho = int(sys.argv[2])

lista_de_arquivos = os.listdir(pasta) #Cria uma lista com os nomes dos arquivos ness pasta
print(lista_de_arquivos)

for arquivo in lista_de_arquivos:
    caminho = os.path.join(pasta,arquivo) #junta o nome da pasta com o nome do arquivo, para criar o caminho completo sem erros. 
    tamanho_do_arquivo = os.path.getsize(caminho) #Devolve o tamanho do arquivo em bytes
    data_segundos = os.stat(caminho).st_mtime #devolve o tempo da ultima modificação do arquivo
    data_entendivel = time.ctime(data_segundos)
    
    if tamanho_do_arquivo > valor_tamanho:
        print(f"O nome do arquivo é {arquivo}, o seu tamanho é: {tamanho_do_arquivo} e a ultima data de modificação foi {data_entendivel}")