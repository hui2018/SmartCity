# import gmplot package
import gmplot
import numpy as np
# generate 700 random lats and lons
latitude = (np.random.random_sample(size = 700) - 0.5) * 180
longitude = (np.random.random_sample(size = 700) - 0.5) * 360
# declare the center of the map, and how much we want the map zoomed in
gmap = gmplot.GoogleMapPlotter(0, 0, 2)
# plot heatmap
gmap.heatmap(latitude, longitude)
gmap.scatter(latitude, longitude, c='r', marker=True)
#Your Google_API_Key
gmap.apikey = "AIzaSyAid6Kk6DZVnu0VNsrDJsmhKwH1pqyiu00"
# save it to html
gmap.draw("c:\\users\\jackc\desktop\\country_heatmap.html")

'''
import csv
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import gmplot

def outputScatter():
    data = pd.read_csv('C:\\Users\\jackc\\Desktop\\ctran\dataMerge.csv')
    df = data.groupby('location_id')
	gmap = gmplot.GoogleMapPlotter(0,0,2)
    counter = 0
    result = []
    result_lon = []
    result_lat = []
    result_calculation = []
    result_lon_static = []
    result_lat_static = []
    result_toSCV = []
    above50ft = 0
    above70ft = 0
    above90ft = 0
    above150ft = 0
    index = 0
    colors = ['r','y','g','b']

    for x,y in df:
        for z in range(y.location_distance.values.size):
            result_lon_static.append(y.y_coordinate.values[z])
            result_lat_static.append(y.x_coordinate.values[z])
            if(y.location_distance.values[z] > 30):
                counter = counter + 1
            if(y.location_distance.values[z] > 50):
                above50ft = above50ft + 1
            if(y.location_distance.values[z] > 70):
                above70ft = above70ft + 1
            if(y.location_distance.values[z] > 90):
                above90ft = above90ft + 1
            if(y.location_distance.values[z] > 150):
                above150ft = above150ft + 1

        cal=counter/(y.location_distance.values.size)
        result.append([y.stop_code.values[0], cal, y.stop_lat.values[0], y.stop_lon.values[0]])
        result_lat.append(y.stop_lat.values[0])
        result_lon.append(y.stop_lon.values[0])
        result_calculation.append(cal)
        result_toSCV.append([y.stop_code.values[0], cal, y.location_distance.values.size, counter, above50ft, above70ft, above90ft, above150ft])
        index = index+1
        above50ft = 0
        above70ft = 0
        above90ft = 0
        above150ft = 0
        counter = 0
    result = sorted(result,key=itemgetter(1), reverse=True)
    result_toSCV = sorted(result_toSCV, key=itemgetter(1), reverse=True)
    plt.scatter(result_lat_static,result_lon_static, c='black')

    code_id = []
    for x in result:
        #code_id.append(x[0])
        #result_calculation.append(x[1])
        #result_lat.append(x[2])
        #result_lon.append(x[3])
        if x[1] > 0.9:
            red = plt.scatter(x[3],x[2], c=colors[0], label='>90%')
            #red = plt.scatter(x[3],x[2], c=colors[0], label=x[0])

        elif x[1] > 0.8:
            yellow = plt.scatter(x[3],x[2], c=colors[1], label='>80%')
            #yellow = plt.scatter(x[3],x[2], c=colors[1], label=x[0])
        elif x[1] > 0.7:
            green = plt.scatter(x[3],x[2], c=colors[2], label='>70%')
            #green = plt.scatter(x[3],x[2], c=colors[2], label=x[0])
        else:
            blue = plt.scatter(x[3],x[2], c=colors[3], label='>60%')
            #blue = plt.scatter(x[3],x[2], c=colors[3], label=x[0])


    with open('C:\\Users\\Jackc\\Desktop\\Ctran\\outputPercentError.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['location_id', 'percent_Error', 'total_count', 'above30ft', 'above50ft', 'above70ft', 'above90ft', 'above150ft'])
        for x in result_toSCV:
            writer.writerow(x)

'''

