import os, shutil
from time import sleep

path="C:\denys"

if os.path.isdir (path):

    if os.listdir(path) == []:
        print("NÃO EXISTEM arquivos no diretório" +" "+ path +".")
    else:
        print("EXISTEM arquivos no diretório" +" "+ path +".")
else:
    print("O diretório" +" "+ path +" não existe.")
    print("--")
    print("Criando o diretório.")
    print("--")
    sleep(2)
    os.mkdir(path)
    print("Diretório criado.")
