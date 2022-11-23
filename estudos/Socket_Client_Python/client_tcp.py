import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print ('Cliente conectado.\n')

namefile = str(input('Digite o arquivo a ser enviado: '))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(10000000)
        if not data:
            break
        file.write(data)
print(f'{namefile} RECBIDO.\n')