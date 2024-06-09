from utils.connect_db import connect_db, close_db
from utils.crypto import encrypt
import pwinput as pw

def insert_user():

    print("CADASTRO DE USUÁRIO\n")

    cpf = input("CPF do vendedor (Apenas números): ")
    user_name = input("Nome de usuário: ")
    password = pw.pwinput("Senha: ", mask = '*')
    user_type = input("Tipo de usuário (administrador ou vendedor)").upper()

    password_crypt = encrypt(password)

    conn, cursor = connect_db()

    sql = "SELECT id_seller FROM seller WHERE cpf = ?"

    id_seller = cursor.execute(sql,[cpf]).fetchone()
    id = id_seller[0]

    sql2 = "INSERT INTO user(id_seller, user_name, password, user_type) VALUES(?, ?, ?, ?)"

    cursor.execute(sql2, [id, user_name, password_crypt, user_type])
    
    close_db()

def list_user():

    conn, cursor = connect_db()

    sql = "SELECT id_user, user_name, user_type FROM user"

    users = cursor.execute(sql).fetchall()

    close_db()

    print("USUÁRIOS CADASTRADOS\n")

    for user in users:

        print(f"ID: {user[0]}    USUÁRIO: {user[1]}    ACESSO: {user[2]}")

def redefinir_password():

    print("REDEFINIÇÃO DE SENHA\n")

    user_name = input("Nome de usuário: ")
    password = pw.pwinput("Nova senha: ", mask = '*')

    password_crypt = encrypt(password)

    conn, cursor = connect_db()

    sql = "UPDATE user SET password = ? WHERE user_name = ?"

    cursor.execute(sql, [password_crypt, user_name])

    close_db()

def delete_user():

    print("EXCLUIR USUÁRIO\n")

    user_name = input("Nome de usuário: ")

    conn, cursor = connect_db()

    user = serch_user(user_name)

    option = input(f"""
                   
                   Tem certeza que deseja excluir o usuário: {user[1]}?
                   
                   1 - Sim
                   2 - Não
                   
                   Digite o número da opção desejada: """)

    if option == 1:

        sql = "DELETE FROM user WHERE user_name = ?"

        cursor.execute(sql, [user])

        close_db()
    
    else:
        pass

def serch_user(user_name):

    conn, cursor = connect_db()

    sql = "SELECT id_user, user_name FROM user WHERE user_name = ?"

    user = cursor.execute(sql, [user_name]).fetchone()

    close_db()

    return user