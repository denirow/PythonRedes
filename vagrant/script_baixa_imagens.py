from time import sleep
import os
import subprocess

def lista_repo_remoto():
    print('\033[31;40mListando todas as boxes disponíveis no repositório online\033[m')
    print ("")
    os.system('vagrant.exe cloud search denirow')
    sleep(3)
    print ("")
    
def lista_repo_local():
    print('\033[31;40mListando todas as boxes disponíveis no repositório local\033[m')
    print ("")
    os.system('vagrant box list')
    sleep(3)
    print ("") 

def baixa_debian11():
    print('\033[31;40mBaixando a box do Debian 11\033[m')
    print ("")
    os.system('vagrant box add denirow/debian11')
    sleep(1)

def baixa_xp():
    print('\033[31;40mBaixando a box do Windows XP SP3\033[m')
    print ("")
    os.system('vagrant box add denirow/winxp')
    sleep(1)

def baixa_win7():
    print('\033[31;40mBaixando a box do Windows 7 PRO\033[m')
    print ("")
    os.system('vagrant box add denirow/win7pro')
    sleep(1)

def baixa_win2k8():
    print('\033[31;40mBaixando a box do Windows 2008 Standard\033[m')
    print ("")
    os.system('vagrant box add denirow/win2k8')
    sleep(1)

opcao = 0
while opcao != 9:
    print ("######################################")
    print ("#  " +  '\033[33;40mScript para baixar boxes Vagrant\033[m' + "  #")
    print ("#    " +     '\033[33;40mAutor: Prof. Denys Alexandre\033[m' + "    #")
    print ("#          " +          '\033[33;40mData: 15.12.2021\033[m' + "          #")
    print ("# " +          '\033[31;40mv1.0\033[m' + "                               #")
    print ("######################################")
        
    try: 
        verifica_vagrant = subprocess.check_call('vagrant --version', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        versao = subprocess.check_output("vagrant --version", shell=True)
        versao = versao.decode("utf-8")
        print("\033[31;40mVersão Vagrant detectada: \033[m" + str(versao))
    except:
        print('\033[31;40mInstalação do Vagrand não encontrada.\033[m')
        print('\033[31;40mBaixe em: https://www.vagrantup.com/downloads\033[m')
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
        lista_repo_remoto()
        
    elif opcao == 2:
        lista_repo_local()
        
    elif opcao == 3:
        baixa_debian11()
        
    elif opcao == 4:
        baixa_xp()
        
    elif opcao == 5:
        baixa_win7()
        
    elif opcao == 6:
        baixa_win2k8()
        
    elif opcao == 7:
        print('\033[31;40mBaixando todas as boxes do repositório online (Isso vai demorar ... pega o café e espera)\033[m')
        print ("")
        baixa_debian11()
        baixa_xp()
        baixa_win7()
        baixa_win2k8()

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