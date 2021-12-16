from os import system
from time import sleep
import os
import subprocess

opcao = 8

while opcao != 9:
    print ("######################################")
    print ("#  " +  '\033[33;40mScript para baixar boxes Vagrant\033[m' + "  #")
    print ("#    " +     '\033[33;40mAutor: Prof. Denys Alexandre\033[m' + "    #")
    print ("#          " +          '\033[33;40mData: 15.12.2021\033[m' + "          #")
    print ("# " +          '\033[31;40mv1.0\033[m' + "                               #")
    print ("######################################")
        
    try: 
        verifica_vagrant = subprocess.check_call('vagrant.exe --version', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        versao = subprocess.check_output("vagrant.exe --version", shell=True)
        versao = versao.decode("utf-8")
        print("Versão detectada: " + str(versao))
    except:
        print('\033[31;40mInstalação do Vagrand não encontrada.\033[m')
        print('')
    
    print ("Escolha a opção que deseja:")
    print ("")
    print ("(1) Listar todas as boxes disponíveis no repositório online;")
    print ("(2) Listar todas as boxes disponíveis no repositório local;")
    print ("(3) Baixar a box do Debian 11;")
    print ("(4) Baixar a box do Windows XP SP3;")
    print ("(5) Baixar a box do Windows 7 PRO;")
    print ("(6) Baixar a box do Windows 2008 Standard;")
    print ("(7) Baixar todas as boxes do repositório online (Isso vai demorar ... pega o café e espera)")
    print ("(8) Limpar a tela")
    print ("(9) Sair do script.")
    print ("")
    
    opcao =  int(input("O que você deseja fazer ? "))
    os.system('cls')
    
    if opcao == 1:
        print('\033[31;40mListando todas as boxes disponíveis no repositório online\033[m')
        print ("")
        os.system('vagrant.exe cloud search denirow')
        sleep(3)
        print ("")
    elif opcao == 2:
        print('\033[31;40mListando todas as boxes disponíveis no repositório local\033[m')
        print ("")
        os.system('vagrant.exe box list')
        sleep(3)
        print ("") 
    elif opcao == 3:
        print('\033[31;40mBaixando a box do Debian 11\033[m')
        print ("")
        os.system('vagrant.exe box add denirow/debian11')
        sleep(1)
    elif opcao == 4:
        print('\033[31;40mBaixando a box do Windows XP SP3\033[m')
        print ("")
        os.system('vagrant.exe box add denirow/winxp')
        sleep(1)
    elif opcao == 5:
        print('\033[31;40mBaixando a box do Windows 7 PRO\033[m')
        print ("")
        os.system('vagrant.exe box add denirow/win7pro')
        sleep(1)
    elif opcao == 6:
        print('\033[31;40mBaixando a box do Windows 2008 Standard\033[m')
        print ("")
        os.system('vagrant.exe box add denirow/win2k8')
        sleep(1)
    elif opcao == 7:
        print('\033[31;40mBaixando todas as boxes do repositório online (Isso vai demorar ... pega o café e espera)\033[m')
        print ("")
        print('\033[31;40mBaixando a box do Debian 11\033[m')
        os.system('vagrant.exe box add denirow/debian11')
        print("")
        print("")
        print('\033[31;40mBaixando a box do Windows XP SP3\033[m')
        os.system('vagrant.exe box add denirow/winxp')
        print("")
        print("")
        print('\033[31;40mBaixando a box do Windows 7 PRO\033[m')
        os.system('vagrant.exe box add denirow/win7pro')
        print("")
        print("")
        print('\033[31;40mBaixando a box do Windows 2008 Standard\033[m')
        os.system('vagrant.exe box add denirow/win2k8')
        print("")
        print("")
        sleep(1)
    elif opcao == 8:
        print('Limpando a tela')
        print ("")
        os.system('cls')
    elif opcao == 9:
        print("Saindo o script. Vlw. Flw.")
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
        print ("")
        sleep(2)
