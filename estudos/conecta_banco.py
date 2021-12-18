import mysql.connector
from mysql.connector import errorcode

conexao = mysql.connector.connect(host='192.168.56.101', database='estudos', user='denirow', password='abc@123')
conectou = conexao.is_connected()

if conectou == True:
    banco='SGBD conectado com sucesso!'
    print(banco)
    cursor = conexao.cursor()
    cursor.execute("select * from tb_user where user_name='denys'")
    resultado = cursor.fetchall()
    print(resultado)
else:
    print('Banco de dados não conectado.')


