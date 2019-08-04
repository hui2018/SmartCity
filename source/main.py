import csv
import pandas as pd
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np

'''load csv and sort the location_id for both mean and medium so we can do do the calculation in a for loop'''
data = pd.read_csv('C:\\Users\\Jack\\Desktop\\DataScience\\Ctran\\data_merge.csv')
df = data.groupby('location_id')

counter = 0
percent_result = 0
result = []
result_lon = []
result_lat = []
result_calculation = []
index = 0

for x,y in df:
    #print(x)
    for z in range(y.location_distance.values.size):
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
for x in result:
    '''maybe scatter plot in here'''
    result_calculation.append(x[1])
    result_lat.append(x[2])
    result_lon.append(x[3])


t = np.arange(result_lat.__len__())
plt.scatter(result_lon, result_lat, c=t)
plt.colorbar();
plt.show()
#print (result)

