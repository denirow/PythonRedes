import os

caminho = "D://programas//teste"
lista_arquivos = os.listdir(caminho)

#print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".png" and ".txt" in arquivo:
        send_email = "contem_png"
    else:
        send_email = "n_contem_png"

print(send_email)