import os.path
import os
import subprocess

try: 
    verifica_vagrant = subprocess.check_call('vagrant.exe --version', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(verifica_vagrant)
except:
    print('nada instalado')

