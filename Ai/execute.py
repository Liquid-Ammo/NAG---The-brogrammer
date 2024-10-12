def execute(a):
    import mysql.connector as sql

    con = sql.connect(host="localhost", user="root", passwd="root")
    if con.is_connected():
        print("Connection Established")
    else:
        print("Connection Error")
    cursor = con.cursor()
    cursor.execute(a)
    output= cursor.fetchall()
    con.close()
    return output
