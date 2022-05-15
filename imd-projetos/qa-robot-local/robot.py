import os
from time import sleep
from datetime import datetime

path = "/root/robot/imagens"
now = datetime.now()
date = now.strftime("%d_%m_%Y")
time = now.strftime("%H_%M_%S")

if os.path.isdir (path):

    if os.listdir(path) == []:
        print("NAO EXISTEM arquivos no diretorio" +" "+ path +".")
    else:
        print("EXISTEM arquivos no diretorio" +" "+ path +".")
        print("--")
        print("Compactando para enviar por email")
        os.system("tar vzcf /root/robot/log_robot_" +""+ date +"_"+""+ time +".tar.gz /root/robot/imagens/")
        print("--")
        print("Excluindo arquivos.")
        sleep(2)
        os.system("rm -rfv" +" "+ path +"/*")
        print("Arquivos excluidos.")
else:
    print("O diretorio" +" "+ path +" nao existe.")
    print("--")
    print("Criando o diretorio.")
    print("--")
    sleep(2)
    os.system("mkdir" +" "+ path +"")
    print("Diretorio criado.")