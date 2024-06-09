from utils.connect_db import connect_db, close_db
from menus.menus_funtions import limpa_terminal

def insert_book():

    print("CADASTRAR LIVRO\n")

    ISBN = input("ISBN: ")
    title = input("Titulo: ").upper()
    writer = input("Autor: ").upper()
    gender = input("Genero: ").upper()
    public_year = input("Ano da publicação: ")
    quantity = int(input("Quantidade em estoque: "))
    price = float(input("Preço: "))

    conn, cursor = connect_db()

    sql = """INSERT INTO book(ISBN, title, writer, gender, public_year, quantity, price)
    VALUES (?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(sql, [ISBN, title, writer, gender, public_year, quantity, price])
    
    close_db

def list_book():

    conn, cursor = connect_db()

    sql = "SELECT * FROM book"

    books = cursor.execute(sql).fetchall()

    close_db()

    print("LIVROS CADASTRADOS\n")

    for book in books:

        print(f"\033[1;96m ID: \033[0;0m{book[0]} \033[1;96m ISBN: \033[0;0m{book[1]} \033[1;96m TITULO: \033[0;0m{book[2]} \
\033[1;96m AUTOR: \033[0;0m{book[3]} \033[1;96m GENERO: \033[0;0m{book[4]} \033[1;96m ANO: \033[0;0m{book[5]} \
\033[1;96m ESTOQUE: \033[0;0m{book[6]} \033[1;96m PREÇO: \033[0;0mR$ {book[7]:.2f}")

def search_book():

    print("BUSCAR LIVRO\n")

    isbn = input("ISBN do livro: ")

    conn, cursor = connect_db()

    sql = "SELECT * FROM book WHERE ISBN = ?"

    book = cursor.execute(sql, [isbn]).fetchone()

    close_db()

    limpa_terminal()

    print("RESULTADO DA BUSCA:\n")

    print(f"\033[1;96m ID: \033[0;0m{book[0]} \033[1;96m ISBN: \033[0;0m{book[1]} \033[1;96m TITULO: \033[0;0m{book[2]} \
\033[1;96m AUTOR: \033[0;0m{book[3]} \033[1;96m GENERO: \033[0;0m{book[4]} \033[1;96m ANO: \033[0;0m{book[5]} \
\033[1;96m ESTOQUE: \033[0;0m{book[6]} \033[1;96m PREÇO: \033[0;0mR$ {book[7]:.2f}")