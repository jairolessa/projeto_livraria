from utils.connect_db import connect_db, close_db

def autentication(user_name):

    conn, cursor = connect_db()

    sql = "SELECT user_name, user_type, password FROM user WHERE user_name = ?"

    info_user = cursor.execute(sql, [user_name]).fetchone()

    close_db()

    return info_user