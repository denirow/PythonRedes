import socket
import requests
import json
from termcolor import colored

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

def enviar_mensagem_slack(webhook_url, mensagem):
    payload = {"text": mensagem}
    headers = {'Content-type': 'application/json'}
    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print("Mensagem enviada para o Slack com sucesso!")
    else:
        print(f"Erro ao enviar mensagem para o Slack. Status code: {response.status_code}")

# Teste de conexão com um host e porta específicos
host = 'www.globo.com'  # Insira o host que você deseja testar
porta = 80  # Insira a porta que você deseja testar

if testar_conexao(host, porta):
    srv = "*SERVIDOR RETAIL PRODUÇÃO*"
    mensagem = f"{srv}\n*SERVIÇOS TESTADOS*\nHost: {host} Porta: {porta} : PASSED"
    print(mensagem)
else:
    mensagem = f"A conexão falhou para {host} na porta {porta}."
    print(mensagem)

# Insira o seu webhook URL do Slack
https://hooks.slack.com/services/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

# Envia a mensagem para o canal do Slack
enviar_mensagem_slack(webhook_url, mensagem)