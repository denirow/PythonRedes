import mysql.connector
from mysql.connector import errorcode

conexao = mysql.connector.connect(host='192.168.56.101', database='estudos', user='denirow', password='abc@123')

if conexao.is_connected():
    banco='SGBD conectado com sucesso!'
    print(banco)
    cursor = conexao.cursor()
    cursor.execute("select * from tb_user where user_name='denys'")

resultado = cursor.fetchall()
print(resultado)