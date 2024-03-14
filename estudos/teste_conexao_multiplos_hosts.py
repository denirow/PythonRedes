import socket
import requests
import json
import datetime

agora = datetime.datetime.now()
data_atual = datetime.date.today()
hora_formatada = agora.strftime("%H:%M")
data_formatada = data_atual.strftime("%d/%m/%Y")


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

# Lista de hosts e portas a serem testados
hosts = ['www.uol.com.br', 'www.globo.com', 'www.ifrn.edu.br']  # Insira os hosts que você deseja testar
portas = [80, 80, 8823]  # Insira as portas que você deseja testar
nome_svcs = ['Protheus', 'Jira', 'BCA']

# Insira o seu webhook URL do Slack
# Canal devops-pvt
# webhook_url = 'https://hooks.slack.com/services/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'
# Pessoal Denys Alexandre 
webhook_url = 'https://hooks.slack.com/services/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' 


# Verifica se os arrays de hosts e portas têm o mesmo comprimento
if len(hosts) != len(portas):
    print("Erro: Os arrays de hosts e portas têm comprimentos diferentes.")
    exit()

# Itera sobre os hosts e portas e testa a conexão
for i in range(len(hosts)):
    host = hosts[i]
    porta = portas[i]
    nome_svc = nome_svcs[i]
    
    if testar_conexao(host, porta):
        mensagem = f"*ORIGEM: SERVIDOR RETAIL PRODUÇÃO*\nServiço: {nome_svc}\nHost: {host} Porta: {porta}\n*Status:* OK\nHora do teste: {data_formatada} {hora_formatada}"
        print(mensagem)
    else:
        mensagem = f"*ORIGEM: SERVIDOR RETAIL PRODUÇÃO*\nServiço: {nome_svc}\nHost: {host} Porta: {porta}\n*Status:* FAIL\nHora do teste: {data_formatada} {hora_formatada}"
        print(mensagem)

    # Envia a mensagem para o canal do Slack
    enviar_mensagem_slack(webhook_url, mensagem)
