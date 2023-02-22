from imap_tools import MailBox, AND
from datetime import datetime

login = "denirowtestes@gmail.com"
# Senha de APP do Gmail
senha = "qtesmrspmskfzgfo"
caixa = MailBox("imap.gmail.com").login(login, senha)

#Filtrando e emails
lista_email = caixa.fetch(AND(from_="denirow@gmail.com", subject="update_bca"))
for email in lista_email:
    print(email.subject)
    print("")

lista_email = caixa.fetch(AND(from_="denirow@gmail.com", subject="update_bca"))
quantidade = len(list(lista_email))
quantidade = str(quantidade)
print("A quantidade de emails encontrados foi: " + quantidade)

lista_anexos = caixa.fetch(AND(from_="denirow@gmail.com"))
for att in lista_anexos:
    if len(att.attachments) > 0:
        for anexo in att.attachments:
            if "fatura.pdf" in anexo.filename:
                info_anexo = anexo.payload
                with open("tabela_criada.pdf", "wb") as arquivo_tabelas:
                    arquivo_tabelas.write(info_anexo)
                    print("Arquivo criado com sucesso!")

now = datetime.now()
date = now.strftime("%d_%m_%Y")
print("Data de execução da rotina: " + date)

