from imap_tools import MailBox, AND
from datetime import datetime
from time import sleep
import os

# Login do Gmail
login = "denirowtestes@gmail.com"
# Senha de APP do Gmail
senha = "qtesmrspmskfzgfo"
# Variaveis do email de origem
origem = "denirow@gmail.com"
subject = "update_bca"
print('')
print("INICIANDO SCRIPT DE ATUALIZAÇÃO DO BCA VIA EMAIL")
print('')
print("Buscando por emails novos ...")
print('')
caixa = MailBox("imap.gmail.com").login(login, senha)

# Funcao Data
def data():
    now = datetime.now()
    date = now.strftime("%d_%m_%Y")
    print("Data de execução da rotina: " + date)

# Funcao para limpar a caixa de entrada
def limpa_email():
    uids = []
    for msg in caixa.fetch(AND(from_= origem, subject= subject)):
        uids.append(msg.uid)
    print("Deletando EMAIL.")
    caixa.delete(uids)

# Funcao Iniciando processo de descompactação do arquivo e execução da atualização do BCA
def extrair_tabelas():
    print("")
    print('INICIADO: PROCESSO DE EXTRAÇÃO DAS TABELAS')
    sleep(2)
    print("")
    os.system('unzip tabelas.zip -d data/BCA/')
    print("")
    os.system('rm tabelas.zip')
    print('FINALIZADO: PROCESSO DE EXTRAÇÃO DAS TABELAS')
    sleep(1)

# Funcao para iniciar o processo de atualização do BCA
def update_bca():
    print("")
    print('INICIADO: PROCESSO DE ATUALIZAÇÃO DO BCA')
    print('')
    os.system('python3 scripts/teste.py')
    print("")
    print('FINALIZADO: PROCESSO DE ATUALIZAÇÃO DO BCA')
    print("")
    sleep(1)

#Listando a quantidade de emails que atendem o filtro.
lista_email = caixa.fetch(AND(from_= origem, subject= subject))
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
    for msg in caixa.fetch(AND(from_= origem, subject= subject)):
        print(msg.uid, msg.date_str, msg.from_, msg.subject)    
        print("")  

#Localizando o email com o anexo das tabelas e baixando o arquivo.
# Caso o email não contenha anexo ou o anexo seja inválido, ele será excluído.
lista_anexos = caixa.fetch(AND(from_= origem, subject= subject))
for att in lista_anexos:
    if len(att.attachments) > 0:
        for anexo in att.attachments:
            if "tabelas.zip" in anexo.filename:
                info_anexo = anexo.payload
                with open("tabelas.zip", "wb") as arquivo_tabelas:
                    arquivo_tabelas.write(info_anexo)
                    print("Download do anexo TABELAS.ZIP feito com sucesso.")
                    extrair_tabelas()
                    update_bca()
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
    for msg in caixa.fetch(AND(from_= origem, subject= subject)):
        uids.append(msg.uid)
    print("Deletando EMAIL e finalizando o script.")
    now = datetime.now()
    date = now.strftime("%d_%m_%Y")
    print("Script finalizado por falta de anexo: " + date)
    caixa.delete(uids)
    quit()

#Limpando Caixa de Email
uids = []
for msg in caixa.fetch(AND(from_= origem, subject= subject)):
    uids.append(msg.uid)
print("Deletando EMAIL.")
caixa.delete(uids)
data()