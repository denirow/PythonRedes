import os

ns = "feature"
id = "1776"
system = "backend"

# Comando completo do kubectl
get_kube = os.popen("kubectl get pods -n " + ns + "| grep " + id + " | grep " + system).read()
print('Aqui é a saída do comando completo')
print(get_kube.split())
print()

# Split da primeira parte da saída
get_kube = get_kube.split()
get_kube = get_kube[0]
get_kube = get_kube.split("-")
print("Aqui é a primeira parte do comando splitado")
print(get_kube)
print()

# Lendo e printando parte do split
print("Aqui é o filtro da primeira parte do comando splitado")
print(get_kube[2])
print()

if (get_kube[1]) == "backend":
    print("aqui é o backend")
else:
    print("aqui não é o backend")