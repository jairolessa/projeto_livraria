import pwinput as pw
from utils import seller, user, book
import os

def limpa_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def tela_login():

    print("\033[1;95m LOGIN \033[0;0m\n")
    
    user_name = input("\033[1;95m Usuário: \033[0;0m")
    
    password = pw.pwinput("\033[1;95m Senha: \033[0;0m", mask = "*")

    return user_name, password

def menu_principal_adm():

    print("""
        
       \033[1;95m MENU PRINCIPAL \033[0;0m            
        
       \033[1;96m[1]\033[0;0m Vendedores.             
       \033[1;96m[2]\033[0;0m Usuários.               
       \033[1;96m[3]\033[0;0m Livros.                 
       \033[1;96m[4]\033[0;0m Vendas.  
                  
        """)
    
    option = int(input('\033[1;96m Digite o número correspondente a opção desejada: \033[0;0m'))
    return option

def menu_principal_std():

    print("""
        
       \033[1;95m MENU PRINCIPAL \033[0;0m    
        
       \033[1;95m[1]\033[0;0m Usuário.                
       \033[1;95m[2]\033[0;0m Livros.                
       \033[1;95m[3]\033[0;0m Vendas.       
             
        """)
    
    option = int(input('\033[1;95m Digite o número correspondente a opção desejada: \033[0;0m'))
    return option

def menu_seller():

    print("""
        
       \033[1;92m VENDEDOR \033[0;0m                  
        
       \033[1;92m[1]\033[0;0m Cadastrar.              
       \033[1;92m[2]\033[0;0m Listar.                 
       \033[1;92m[3]\033[0;0m Buscar.                 
                 
        """)
    
    option = int(input('\033[1;92m Digite o número correspondente a opção desejada: \033[0;0m'))
    
    match option:

        case 1:
            limpa_terminal()
            seller.insert_seller()
        case 2:
            limpa_terminal()
            seller.list_seller()
        case 3:
            limpa_terminal()
            seller.serch_seller()

def menu_adm_user():

    print("""
        
       \033[1;93m USUÁRIO \033[0;0m                   
        
       \033[1;93m[1]\033[0;0m Cadastrar.               
       \033[1;93m[2]\033[0;0m Listar.                 
       \033[1;93m[3]\033[0;0m Redefinir senha.        
       \033[1;93m[4]\033[0;0m Remover.                
            
        """)
    
    option = int(input('\033[1;93m Digite o número correspondente a opção desejada: \033[0;0m'))
    
    match option:

        case 1:
            limpa_terminal()
            user.insert_user()
        case 2:
            limpa_terminal()
            user.list_user()
        case 3:
            limpa_terminal()
            user.redefinir_password()
        case 4:
            limpa_terminal()
            user.delete_user()


def menu_std_user():

    print("""
        
       \033[1;90m[1]\033[0;0m Redefinir Senha.                |
                 
        """)
    
    option = int(input('\033[1;93m Digite o número correspondente a opção desejada: \033[0;0m'))
    
    match option:
        case 1:
            limpa_terminal()
            user.redefinir_password()

def menu_book():

    print("""
        
       \033[1;94m LIVRO \033[0;0m                    
        
       \033[1;94m[1]\033[0;0m Cadastrar.             
       \033[1;94m[2]\033[0;0m Listar.                
       \033[1;94m[3]\033[0;0m Buscar.               
                
        """)
    
    option = int(input('\033[1;94m Digite o número correspondente a opção desejada: \033[0;0m'))
    
    match option:

        case 1:
            limpa_terminal()
            book.insert_book()
        case 2:
            limpa_terminal()
            book.list_book()
        case 3:
            limpa_terminal()
            book.search_book()
        case 4:
            limpa_terminal()
            book.delete_book()

def menu_sell():

    print("""
       
        \033[1;90m[1]\033[0;0m Listar.                
               
        """)
    
    option = int(input('\033[1;93m Digite o número correspondente a opção desejada: \033[0;0m'))