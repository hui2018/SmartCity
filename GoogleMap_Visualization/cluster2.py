import csv
import math
import pandas as pd

# import gmplot package 
import gmplot 

import load_csv1 as load_csv

# sampleData = "stop101.csv" # location_id, x_coord, y_coord
sampleData = "stop2329.csv" # location_id, x_coord, y_coord

sd = load_csv.loadSampleData(sampleData)

lat_list = []
long_list = []

lat_list = sd.y_coord
long_list = sd.x_coord

gmap5 = gmplot.GoogleMapPlotter(sd.y_coord[0], sd.x_coord[0], 13) 
gmap5.scatter( lat_list, long_list, '# FF0000', size = 2, marker = False) # size represents circle radius (i think)

# polygon method Draw a polygon with 
# the help of coordinates 
gmap5.polygon(lat_list, long_list, color = 'cornflowerblue')    
  
gmap5.draw( "C:\\Users\\Mkwon\\Desktop\\stops_2329a.html" ) 