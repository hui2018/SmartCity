import csv
import pandas as pd
from operator import itemgetter
from scipy import stats
def pvalue():
    '''load csv and sort the location_id for both mean and medium so we can do do the calculation in a for loop'''
    data = pd.read_csv('C:\\Users\\Jack\\Desktop\\DataScience\\Ctran\\data_merge.csv')
    df = data.groupby('location_id')

    pvalueList = []
    #print(stats.ttest_1samp([1,2,3,4,5], 1))
    for x,y in df:
        pvalueList.append([y.stop_code.array[0], stats.ttest_1samp(y.x_coordinate.array, y.stop_lon.array[0])[0], stats.ttest_1samp(y.x_coordinate.array, y.stop_lon.array[0])[1],stats.ttest_1samp(y.y_coordinate.array, y.stop_lat.array[0])[0], stats.ttest_1samp(y.y_coordinate.array, y.stop_lat.array[0])[1]])

    pvalueList = sorted(pvalueList, key=itemgetter(2), reverse=False)

    with open('C:\\Users\\Jack\\Desktop\\DataScience\\Ctran\\outputpValue.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['location_id', 'x_statistics','x_p-value', 'y_statistics', 'y_p-value'])
        for x in pvalueList:
            writer.writerow(x)

    #for z in pvalueList:
     #   print(z)

if __name__ == "__main__":
    pvalue()
