import os
from time import sleep

path="C:\denys"
rm_win="del" +" "+ path +"\* /Q"

if os.path.isdir (path):

    if os.listdir(path) == []:
        print("NÃO EXISTEM arquivos no diretório" +" "+ path +".")
    else:
        print("EXISTEM arquivos no diretório" +" "+ path +".")
        print("--")
        print("Excluindo arquivos.")
        sleep(2)
        os.system(rm_win)
        print("Arquivos excluídos.")
    
else:
    print("O diretório" +" "+ path +" não existe.")
    print("--")
    print("Criando o diretório.")
    print("--")
    sleep(2)
    os.mkdir(path)
    print("Diretório criado.")
