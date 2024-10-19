def execute(a):
    import mysql.connector as sqltor
    con=sqltor.connect(host='localhost',user='root',passwd='root')
    if con.is_connected():
        print('Connection Secure')
    else:
        print('Connection Error')
    cursor=con.cursor()
    cursor.execute(a)
    data=cursor.fetchall()
    print(data)
    con.close()