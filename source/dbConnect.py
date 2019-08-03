import psycopg2

def connect():
    conn = psycopg2.connect(
        database = "ctran",
        user = "jack",
        password = "test",
        host = "localhost",
        port = "5432"
    )
    return conn
