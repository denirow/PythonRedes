import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Server
host = "smtp.gmail.com" 
port = "587"
login = "denirowtestes"
senha = "D3nys0781=,="

server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.login(login,senha)
#Server

#Email
corpo = "Pedão, esse vai ser o formato do email que será enviado pelo script. Blz ? Depois mando com o anexo."
email_msg = MIMEMultipart()

email_msg['From'] = login
email_msg['To'] = 'denirow@gmail.com'
email_msg['Subject'] = 'Log Robot Projeto Smarter. Data: 09/05/2022'
email_msg.attach(MIMEText(corpo,'plain'))
#Email

#Envio
server.sendmail(email_msg['From'],email_msg["To"],email_msg.as_string())
server.quit()
#Envio