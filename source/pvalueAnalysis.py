import csv
import pandas as pd
from operator import itemgetter
from scipy import stats
def pvalue():
    '''load csv and sort the location_id for both mean and medium so we can do do the calculation in a for loop'''
    data = pd.read_csv('C:\\Users\\Jackc\\Desktop\\Ctran\\dataMerge.csv')
    df = data.groupby('location_id')
    pvalueList = []
    for x,y in df:
        pvalueList.append([y.stop_code.array[0], stats.ttest_1samp(y.x_coordinate.array, y.stop_lon.array[0])[0], stats.ttest_1samp(y.x_coordinate.array,
                            y.stop_lon.array[0])[1],stats.ttest_1samp(y.y_coordinate.array, y.stop_lat.array[0])[0], stats.ttest_1samp(y.y_coordinate.array, y.stop_lat.array[0])[1]])

    pvalueList = sorted(pvalueList, key=itemgetter(2), reverse=False)

    with open('C:\\Users\\Jackc\\Desktop\\Ctran\\outputpValue.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['location_id', 'x_statistics','x_p-value', 'y_statistics', 'y_p-value'])
        for x in pvalueList:
            writer.writerow(x)
if __name__ == "__main__":
    pvalue()
