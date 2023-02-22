from imap_tools import MailBox, AND
from datetime import datetime

# Login do Gmail
login = "denirowtestes@gmail.com"
# Senha de APP do Gmail
senha = "qtesmrspmskfzgfo"
caixa = MailBox("imap.gmail.com").login(login, senha)

# Funcao Data
def data():
    now = datetime.now()
    date = now.strftime("%d_%m_%Y")
    print("Data de execução da rotina: " + date)

# Funcao para limpar a caixa de entrada
def limpa_email():
    uids = []
    for msg in caixa.fetch(AND(from_="denirow@gmail.com" , subject="update_bca")):
        uids.append(msg.uid)
    print("Deletando EMAIL.")
    caixa.delete(uids)

#Listando a quantidade de emails que atendem o filtro.
lista_email = caixa.fetch(AND(from_="denirow@gmail.com", subject="update_bca"))
quantidade = len(list(lista_email))

# Vericando se a caixa de entrada esta zerada
quantidade = int(quantidade)
if quantidade == 0:
    print("####################################")
    print("# NENHUM EMAIL NOVO FOI ENCONTRADO #")
    print("####################################")
    data()
    quit()

# Identificando se existe mais de um email que obedeça o filtro.
# Se houver, todos os emails serão excluídos
quantidade = int(quantidade)
if quantidade > 1:
    quantidade = str(quantidade)
    print("Emails encontrados: " + quantidade)
    print("#################################################################")
    print("# Foram encontrados multiplos emails que se encaixam no filtro. #") 
    print("# A caixa de entrada será zerada. Você deve enviar outro email. #")
    print("#################################################################")
    limpa_email()
    data()
    quit()

# Verificando se só existe um email que obedeça os filtros
if quantidade == 1:  
    quantidade = str(quantidade)
    print("Email encontrado: " + quantidade)
    print("Dados do email encontrado.")
    for msg in caixa.fetch(AND(from_="denirow@gmail.com" , subject="update_bca")):
        print(msg.uid, msg.date_str, msg.from_, msg.subject)    
        print("")  

#Localizando o email com o anexo das tabelas e baixando o arquivo.
# Caso o email não contenha anexo ou o anexo seja inválido, ele será excluído.
lista_anexos = caixa.fetch(AND(from_="denirow@gmail.com" , subject="update_bca"))
for att in lista_anexos:
    if len(att.attachments) > 0:
        for anexo in att.attachments:
            if "tabelas.zip" in anexo.filename:
                info_anexo = anexo.payload
                with open("tabelas.zip", "wb") as arquivo_tabelas:
                    arquivo_tabelas.write(info_anexo)
                    print("Download do anexo TABELAS.ZIP feito com sucesso.")
                    limpa_email()
                    data()
                    quit()                  
            else:
                print("Anexo válido não encontado. Finalizando script.")
                limpa_email()
                data()
                quit()

    # Caso o email atenda os filtros mas não tenha anexo, ele será deletado.          
    if len(att.attachments) == 0:
        print("O email não contém nenhum arquivo anexado.")
    uids = []
    for msg in caixa.fetch(AND(from_="denirow@gmail.com" , subject="update_bca")):
        uids.append(msg.uid)
    print("Deletando EMAIL e finalizando o script.")
    now = datetime.now()
    date = now.strftime("%d_%m_%Y")
    print("Script finalizado por falta de anexo: " + date)
    caixa.delete(uids)
    quit()

#Limpando Caixa de Email
uids = []
for msg in caixa.fetch(AND(from_="denirow@gmail.com" , subject="update_bca")):
    uids.append(msg.uid)
print("Deletando EMAIL.")
caixa.delete(uids)
data()



