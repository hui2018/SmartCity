import csv
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

def outputScatter():
    '''load csv and sort the location_id for both mean and medium so we can do do the calculation in a for loop'''
    data = pd.read_csv('C:\\Users\\Jack\\Desktop\\DataScience\\Ctran\\data_merge.csv')
    df = data.groupby('location_id')

    counter = 0
    result = []
    result_lon = []
    result_lat = []
    result_calculation = []
    result_lon_static = []
    result_lat_static = []

    index = 0
    colors = ['r','y','g','b']

    '''store all values needs into an array and loop through later'''
    for x,y in df:
        for z in range(y.location_distance.values.size):
            '''displaying dynamic stops'''
            #result_lon_static.append(y.y_coordinate.values[z])
            #result_lat_static.append(y.x_coordinate.values[z])
            if(y.location_distance.values[z] > 30):
                counter = counter + 1
        cal=counter/(y.location_distance.values.size)
        result.append([y.stop_code.values[0],cal,y.stop_lat.values[0], y.stop_lon.values[0]])
        result_lat.append(y.stop_lat.values[0])
        result_lon.append(y.stop_lon.values[0])
        result_calculation.append(cal)
        index = index+1
        counter = 0
    result = sorted(result,key=itemgetter(1), reverse=True)
    #plt.scatter(result_lat_static,result_lon_static, c='black')
    '''plot one point at a time by checking what type of color they are'''
    for x in result:
        '''maybe scatter plot in here'''
        result_calculation.append(x[1])
        result_lat.append(x[2])
        result_lon.append(x[3])
        if x[1] > 0.9:
            red = plt.scatter(x[3],x[2], c=colors[0], label='>90%')
        elif x[1] > 0.8:
            yellow = plt.scatter(x[3],x[2], c=colors[1], label='>80%')
        elif x[1] > 0.7:
            green = plt.scatter(x[3],x[2], c=colors[2], label='>70%')
        else:
            blue = plt.scatter(x[3],x[2], c=colors[3], label='>60%')

    '''plot the graph with legends'''
    plt.title('Percentage of bus stopping above 30ft away from stop location')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(handles=[red, yellow, green, blue])
    plt.show()


