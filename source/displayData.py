import dbConnect as a
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats



def main():
    conn = a.connect()


    cursor = conn.cursor()
    postgreSQL_select_Query = "select * from ctran_march"
    cursor.execute(postgreSQL_select_Query)
    result = cursor.fetchall()
    '''
    field_list = [i[0] for i in cursor.description]
    for field_name in field_list:
        if(field_name == 'x_coordinate'):
            print(field_name)
    '''

    b = []
    c = []
    for row in result:
        if(row[1] == 2):
            continue
        b.append(row[22])
        c.append(row[23])
        #plt.scatter(row[22],row[23], c="b")

    cursor1 = conn.cursor()
    postgreSQL_select_Query1 = "select * from ctran_march_static"
    cursor1.execute(postgreSQL_select_Query1)
    result1 = cursor1.fetchall()
    d =[]
    e=[]
    t = np.arange(cursor1.rowcount)
    for row in result1:
        d.append(row[4])
        e.append(row[3])

    plt.scatter(b,c,c="r")
    plt.scatter(d,e,c=t, edgecolors="black")
    plt.show()

if __name__ == "__main__":
    main()
