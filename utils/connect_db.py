import sqlite3

def connect_db():
    
    global conn, cursor

    try:

        conn = sqlite3.connect('db_livraria.sqlite')
        cursor = conn.cursor()

        return conn, cursor
    
    except sqlite3.OperationalError as error:
        print(f"Não foi possível se conectar com o Banco de Dados. Detalhes: {error}")

def close_db():

    conn.commit()
    cursor.close()
    conn.close()