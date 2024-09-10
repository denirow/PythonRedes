import imaplib
import email
import os
from datetime import datetime

login = "denirowtestes@gmail.com"
# Senha de APP do Gmail
senha = "qtesmrspmskfzgfo"
caixa = imaplib.IMAP4_SSL("imap.gmail.com")
caixa.login(login,senha)
caixa.select("INBOX")
#FILTRAR POR SUBJECT
status, messages = caixa.search(None, 'SUBJECT "update_bca"')
print(messages)
#Imprime data da operação
now = datetime.now()
date = now.strftime("%d_%m_%Y")
print(date)