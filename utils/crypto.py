import bcrypt as bc
import pwinput as pw
from utils.autentication import autentication

def encrypt(password):

    bytes = password.encode('utf-8')
    hashed = bc.hashpw(bytes, bc.gensalt())

    return hashed

def decrypt(password, hashed):

    bytes = password.encode('utf-8')

    return bc.checkpw(bytes, hashed)

# usuario = input("usuario: ")
# senha = pw.pwinput("senha: ", mask = '*')


# # # senha_hash = encrypt(senha)

# # # print(senha_hash)

# user = autentication(usuario)


# # print(user[2])

# if len(user) > 0 and decrypt(senha, user[2]):
#     print("logado")
# else:
#     print("usuario ou senha invalido")