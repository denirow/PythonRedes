import os, func
import smtplib
from time import sleep
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from dados_email import login,senha,host,port
from email import encoders
from dados_email import login,senha,host,port
from datetime import datetime

path = "/root/robot/imagens"
path_tar = "/root/robot/"
now = datetime.now()
date = now.strftime("%d_%m_%Y")
time = now.strftime("%H_%M_%S")

def email_com_erro ():
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(login,senha)

    corpo = """
    Prezados,
    O script do Robot foi executado e alguns erros FORAM ENCONTRADOS. Os erros estão no arquivo compactado em anexo.

    Att,

    Equipe DevOps Projeto Smarter.
    """
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = "denirow@hotmail.com"
    email_msg['Subject'] = "[COM ERRO] Log Robot Projeto Smarter. Data:" +" "+ date +"."
    email_msg.attach(MIMEText(corpo,'plain'))
    server.sendmail(email_msg['From'],email_msg["To"],email_msg.as_string())
    server.quit()
    print('Email COM erro enviado.')

def email_sem_erro ():
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(login,senha)

    corpo = """
    Prezados,
    O script do Robot foi executado, mas NENHUM erro foi encontrado.

    Att,

    Equipe DevOps Projeto Smarter.
    """
    email_msg = MIMEMultipart()

    email_msg['From'] = login
    email_msg['To'] = "denirow@hotmail.com"
    email_msg['Subject'] = "[SEM ERRO] Log Robot Projeto Smarter. Data:" +" "+ date +"."
    email_msg.attach(MIMEText(corpo,'plain'))

    server.sendmail(email_msg['From'],email_msg["To"],email_msg.as_string())
    server.quit()
    print('Email SEM erro enviado.')