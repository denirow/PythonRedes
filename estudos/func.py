import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from dados_email import login,senha,host,port
from email import encoders
from dados_email import login,senha,host,port
from datetime import datetime

path = "/opt/robotframework/results"
path_tar = "/opt/robotframework"
now = datetime.now()
date = now.strftime("%d_%m_%Y")
time = now.strftime("%H_%M_%S")
email = "projetosmarter-testes@imd.ufrn.br"
email_teste = "denirow@hotmail.com"

#Enviar email quando algum arquivo de erro do Robot é gerado.
def email_com_erro ():
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(login,senha)

    corpo = """
    <p>Prezados,<br></p>
    <p>O script do Robot foi executado e alguns <b><font color="red">ERROS FORAM ENCONTRADOS</font></b>. Os erros estão no arquivo compactado em anexo.<br></p>

    <p>Att,<br></p>

    <p><b>Equipe DevOps Projeto Smarter.</b></p>
    """
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email
    email_msg['Subject'] = "[COM ERRO] Log Robot Projeto Smarter. Data:" +" "+ date +"."
    email_msg.attach(MIMEText(corpo,'html'))

    path_arquivo = "/opt/robotframework/log_robot.tar.gz"
    anexo = open(path_arquivo,'rb')

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(anexo.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f'attachment; filename=log_robot.tar.gz')
    anexo.close()
    email_msg.attach(att)

    server.sendmail(email_msg['From'],email_msg["To"],email_msg.as_string())
    server.quit()
    
#Enviar email quando nenhum arquivo de erro do Robot é gerado.
def email_sem_erro ():
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(login,senha)

    corpo = """
    <p>Prezados,<br></p>
    <p>O script do Robot foi executado, mas <b><font color="red">NENHUM</font></b> erro foi encontrado.<br></p>

    <p>Att,<br></p>

    <p><b>Equipe DevOps Projeto Smarter.</b></p>
    """
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = email
    email_msg['Subject'] = "[COM ERRO] isso eh um teste Log Robot Projeto Smarter. Data:" +" "+ date +"."
    email_msg.attach(MIMEText(corpo,'html'))

    server.sendmail(email_msg['From'],email_msg["To"],email_msg.as_string())
    server.quit()
    print("email enviado com sucesso")