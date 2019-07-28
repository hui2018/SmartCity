import dbConnect as a

def main():
    conn = a.connect()

    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from test order by x_coordinate"
    cursor.execute(postgreSQL_select_Query)
    testing = cursor.fetchall()

    for row in testing:
           print("x_coordinate = ", row[0], )
           print("y_coordinate  = ", row[1], "\n")

if __name__ == "__main__":
    main()
