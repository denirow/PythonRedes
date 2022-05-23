from asyncio.constants import LOG_THRESHOLD_FOR_CONNLOST_WRITES
import os

caminho = "D://programas//teste"
lista_arquivos = os.listdir(caminho)

#print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        print("Caminho contem arquivo texto")
    else:
        print("Caminho não contem arquivo texto")