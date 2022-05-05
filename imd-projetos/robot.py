import os

path = "C:\denys"

if os.listdir(path) == []:
    print("Não existem arquivos no diretorio")
else:
    print("Contém arquivos no diretório")