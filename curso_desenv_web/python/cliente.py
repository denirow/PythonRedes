import socket

def main():
    # Configuração do cliente
    host = '127.0.0.1'  # Endereço IP do servidor
    porta = 9999  # Porta em que o servidor está ouvindo

    # Cria um socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Tenta conectar ao servidor
        client_socket.connect((host, porta))
    except ConnectionRefusedError:
        print("Erro: Não foi possível se conectar ao servidor. Verifique se o servidor está ativo.")
        return

    # Solicita ao usuário para inserir dois números inteiros
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    # Envia os números para o servidor
    client_socket.send(str(numero1).encode())
    client_socket.send(str(numero2).encode())

    # Recebe o resultado do servidor
    resultado = client_socket.recv(1024).decode()
    print(f"O resultado da soma é: {resultado}")

    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == '__main__':
    main()
