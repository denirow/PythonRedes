import os

#get_kube = os.system("kubectl get pods -n feature | grep 1776 | grep backend")
get_kube = "smartone-backend-1776-5bd989d599-j4p4s        4/4     Running     0          14h"
print('Aqui eh o comando completo')
print(get_kube.split())
print()

get_kube = get_kube.split()
get_kube = get_kube[0]
get_kube = get_kube.split("-")
print("Aqui é a primeira parte do comando splitado")
print(get_kube)
print()

print("aqui eh o filtro da primeira parte do comando splitado")
print(get_kube[2])
print()

if (get_kube[1]) == "backend":
        print("aqui é o backend")
else:
    print("aqui não é o backend")