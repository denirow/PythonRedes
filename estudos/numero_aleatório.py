import random
import os
import psutil

# Recebe o ID do processo que está executando.
process_id = os.getpid()

# Gere dois números aleatórios entre 1000 e 9999
numero1 = random.randint(1000, 9999)
numero2 = random.randint(1000, 9999)

# Calcule a soma dos dois números
soma = numero1 + numero2

# Apresente os números gerados e a soma
print(f"Primeiro número: {numero1}")
print(f"Segundo número: {numero2}")
print(f"Soma: {soma}")

if soma % 2 == 0:
    print("O número da soma é par.")
    print("")
else:
    print("O número da soma é ímpar.")
    print("")

print("INFORMAÇÕES DO SISTEMA OPERACIONAL")
print(f"ID do processo atual: {process_id}")
try:
    # Obtenha as informações do processo usando o PID
    processo = psutil.Process(process_id)

    # Obtenha o nome de usuário associado ao processo
    username = processo.username()
    print(f"O processo com PID {process_id} pertence ao usuário: {username}")

except psutil.NoSuchProcess:
    print(f"Não foi possível encontrar o processo com PID {process_id}")