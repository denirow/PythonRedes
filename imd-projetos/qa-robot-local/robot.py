import os, func
import smtplib
from time import sleep
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dados_email import login,senha,host,port
from datetime import datetime


path = "/root/robot/imagens"
path_tar = "/root/robot/"
now = datetime.now()
date = now.strftime("%d_%m_%Y")
time = now.strftime("%H_%M_%S")

if os.path.isdir (path):

    if os.listdir(path) == []:
        print("NAO EXISTEM arquivos no diretorio" +" "+ path +".")
        func.email_sem_erro()
    else:
        print("EXISTEM arquivos no diretorio" +" "+ path +".")
        print("--")
        print("Compactando para enviar por email.")
        os.system("tar vzcf /root/robot/log_robot_" +""+ date +""+".tar.gz "+ path +"")
        print("--")
        print("Excluindo arquivos.")
        sleep(2)
        os.system("rm -rfv" +" "+ path +"/*")
        print("Arquivos excluidos.")
        func.email_com_erro()
else:
    print("O diretorio" +" "+ path +" nao existe.")
    print("--")
    print("Criando o diretorio.")
    print("--")
    sleep(2)
    os.system("mkdir" +" "+ path +"")
    print("Diretorio criado.")