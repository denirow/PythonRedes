import socket
import threading

def handle_client(client_socket):
    # Recebe os dois números do cliente
    numero1 = int(client_socket.recv(1024).decode())
    numero2 = int(client_socket.recv(1024).decode())

    # Soma os números
    resultado = numero1 + numero2

    # Envia o resultado de volta para o cliente
    client_socket.send(str(resultado).encode())

    # Fecha a conexão com o cliente
    client_socket.close()

def main():
    # Configuração do servidor
    host = '0.0.0.0'  # Para ouvir em todas as interfaces de rede
    porta = 9999  # Porta em que o servidor vai ouvir

    # Cria um socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket ao endereço e à porta
    server_socket.bind((host, porta))

    # Começa a ouvir por conexões
    server_socket.listen(5)
    print(f"Servidor ouvindo na porta {porta}...")
    print("COM THREAD")

    while True:
        # Aceita uma conexão quando um cliente se conecta
        client_socket, client_address = server_socket.accept()
        print(f"Conexão de {client_address}")

        # Inicia um novo thread para lidar com a conexão do cliente
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()
