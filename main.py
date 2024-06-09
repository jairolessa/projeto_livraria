from menus import menus_funtions as menu
from utils.autentication import autentication
from utils.crypto import decrypt

looping = 0

while looping == 0:

    user_name, password = menu.tela_login()

    logado = autentication(user_name)

    if len(logado) > 0 and decrypt(password, logado[2]):
        
        while True:

            menu.limpa_terminal()

            print(f"BEM VINDO {logado[0]}    NÍVEL DE ACESSO: {logado[1]}")

            if logado[1] == "ADMINISTRADOR":
            
                option_menu_principal = menu.menu_principal_adm()

                match option_menu_principal:

                        case 1:
                            menu.limpa_terminal()
                            menu.menu_seller()
                            turn_menu_principal = int(input("\nRetornar ao menu principal? (1 - SIM; 2 - NÃO): "))
                            
                            if turn_menu_principal == 2:
                                 looping = 1
                                 break
                            else:
                                 pass
                            
                        case 2:
                            menu.limpa_terminal()
                            menu.menu_adm_user()
                            turn_menu_principal = int(input("\nRetornar ao menu principal? (1 - SIM; 2 - NÃO): "))
                            
                            if turn_menu_principal == 2:
                                 looping = 1
                                 break
                            else:
                                 pass
                        case 3:
                            menu.limpa_terminal()
                            menu.menu_book()
                            turn_menu_principal = int(input("\nRetornar ao menu principal? (1 - SIM; 2 - NÃO): "))
                            
                            if turn_menu_principal == 2:
                                 looping = 1
                                 break
                            else:
                                 pass
                        case 4:
                            menu.limpa_terminal()
                            menu.menu_sell()
                            turn_menu_principal = int(input("\nRetornar ao menu principal? (1 - SIM; 2 - NÃO): "))
                            
                            if turn_menu_principal == 2:
                                 looping = 1
                                 break
                            else:
                                 pass
            else:
                
                option_menu_printcipal = menu.menu_principal_adm()

                match option_menu_printcipal:

                        case 1:
                            menu.limpa_terminal()
                            menu.menu_std_user()
                            turn_menu_principal = int(input("\nRetornar ao menu principal? (1 - SIM; 2 - NÃO): "))
                            
                            if turn_menu_principal == 2:
                                 looping = 1
                                 break
                            else:
                                 pass
                        case 2:
                            menu.limpa_terminal()
                            menu.menu_book()
                            turn_menu_principal = int(input("\nRetornar ao menu principal? (1 - SIM; 2 - NÃO): "))
                            
                            if turn_menu_principal == 2:
                                 looping = 1
                                 break
                            else:
                                 pass
                        case 3:
                            menu.limpa_terminal()
                            menu.menu_sell()
                            turn_menu_principal = int(input("\nRetornar ao menu principal? (1 - SIM; 2 - NÃO): "))
                            
                            if turn_menu_principal == 2:
                                 looping = 1
                                 break
                            else:
                                 pass

    else:
         menu.limpa_terminal()
         print("\n\033[91m Usuário ou senha inválidos! \033[0;0m\n")     