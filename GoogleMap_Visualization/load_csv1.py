import csv
import math
import pandas as pd

def loadSampleData(sampleData):
    sample_data = pd.read_csv(sampleData, dtype={'location_id': int, 'x_coord': float, 'y_coord': float})
    return sample_data


def loadInitialStops(initialStops):
    initial_stops = pd.read_csv(initialStops, dtype={'stop_code': int, 'stop_lat': float, 'stop_long': float, 'index': int})
    return initial_stops

def euclidDistance(x1, y1, x2, y2):
    #print("point 1: (", x1, ",", y1, ")")
    #print("point 2: (", x2, ",", y2, ")")
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def binarySearch(arr, l, r, x):
    # print("lower: ", l, "\tupper: ", r)
    # check  base case
    if r >= l:
        mid = l + int((r-l)/2)

        # if element is present at middle itself
        if arr[mid] == x:
            return mid
            
            # if element is smaller than mid, then search left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        # else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
    # element is not present in array   
    else:
        return -1

