import sqlite3 as sq
try:
    # conn= sq.connect(':memory:')
    conn=sq.connect('custo.db')
    c=conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS custo (
              first_name text,
              last_name text,
              email text)
    """)
    c.execute("""INSERT INTO custo VALUES('BHASKAR','KAUSHIK','bsamples@gmail.com')

    """)
    many_customer=[('hi','hello','s@gmail.com'),('ri','ru','ru@gmail.com'),('ri','ru','ru@gmail.com'),]
    c.executemany("INSERT INTO custo VALUES(?,?,?)",many_customer)
    # c.fetchone()
    # c.fetchmany()
    #c.fetchall()

    #Datatypes
    #NULL
    #INTEGER
    #REAL
    #TEXT
    #BLOB
    c.execute("SELECT * FROM custo")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    #close our connection
except sq.Error as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()