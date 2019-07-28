import psycopg2

def connect():
    conn = psycopg2.connect(
        database = "test",
        user = "jack",
        password = "test",
        host = "localhost",
        port = "5432"
    )
    return conn

'''
conn = connect()

cursor = conn.cursor()
postgreSQL_select_Query = "select * from test order by x_coordinate"
cursor.execute(postgreSQL_select_Query)
testing = cursor.fetchall()

for row in testing:
       print("x_coordinate = ", row[0], )
       print("y_coordinate  = ", row[1], "\n")
'''
