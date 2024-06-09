from utils.connect_db import connect_db, close_db

def insert_seller():

    print("CADASTRAR VENDEDOR\n")

    name = input("Nome: ").upper()
    cpf = input("CPF (Apenas números): ")
    admission_date = input("Data de admissão: ")

    conn, cursor = connect_db()

    sql = "INSERT INTO seller(name, cpf, admission_date) VALUES(?, ?, ?)"

    cursor.execute(sql, [name, cpf, admission_date])
    
    close_db()

def list_seller():

    conn, cursor = connect_db()

    sql = "SELECT * FROM seller"

    sellers = cursor.execute(sql).fetchall()

    close_db()

    for seller in sellers:
        print(f"ID: {seller[0]} NOME: {seller[1]} CPF: {seller[2]} ADMISSÃO: {seller[3]}")

def serch_seller():

    option = int(input("""
TELA DE BUSCA
    
1 - Buscar pelo ID
2 - Buscar pelo nome
    
Digine o número a opção dejesada: """).upper())
    
    conn, cursor = connect_db()

    match option:

        case 1:

            id = int(input("\nID do vendedor: "))
            sql = "SELECT * FROM seller WHERE id_seller = ?"
            seller = cursor.execute(sql,[id]).fetchone()

            for sel in seller:
                print(f"ID: {sel[0]}  NOME: {sel[1]} CPF: {sel[2]} ADMISSÃO: {sel[3]}")
        
        case 2:

            name = input("Nome do vendedor: ")
            sql = "SELECT * FROM seller WHERE name LIKE ?"
            sellers = cursor.execute(sql,['%'+name+'%']).fetchall()

            for seller in sellers:
                print(f"ID: {seller[0]}  NOME: {seller[1]} CPF: {seller[2]} ADMISSÃO: {seller[3]}")
    
    close_db()