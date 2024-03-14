import socket

def testar_conexao(host, porta):
    try:
        # Criar um objeto de socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Define um timeout para a conexão
        sock.settimeout(5)
        
        # Tenta se conectar ao host na porta especificada
        sock.connect((host, porta))
        
        # Se a conexão for bem-sucedida, imprime uma mensagem
        print(f"Conexão bem-sucedida com {host} na porta {porta}")
        
        # Fecha o socket
        sock.close()
        
        return True
    except Exception as e:
        # Se ocorrer algum erro durante a conexão, imprime uma mensagem de erro
        print(f"Erro ao conectar a {host} na porta {porta}: {e}")
        return False

# Teste de conexão com um host e porta específicos
host = 'www.uol.com.br'  # Insira o host que você deseja testar
porta = 8077  # Insira a porta que você deseja testar

if testar_conexao(host, porta):
    print("A conexão foi feita com sucesso!")
else:
    print("A conexão falhou.")
