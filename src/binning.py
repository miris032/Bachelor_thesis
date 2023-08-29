import numpy as np
import pandas as pd
from src._loadingdata import load_data


def binning(inputData, intervals):
    data = load_data(inputData)
    max_values = np.max(data, axis=0)
    min_values = np.min(data, axis=0)

    resultArray = []
    for column in range(data.shape[1]):

        # If there are l numbers in this column, and l < intervals from input, we cannot use the intervals as lables.
        l = len(set(data[:, column]))
        if l < intervals:
            bins = [-np.inf] \
                   + [min_values[column] + j * width for j in range(l - 1)] \
                   + [np.inf]
            labels = range(0, l)


        else:
            width = (max_values[column] - min_values[column]) / intervals
            bins = [-np.inf] \
                   + [min_values[column] + j * width for j in range(intervals-1)] \
                   + [np.inf]

            '''print(f"Column {column + 1}: Min = {min_values[column]}, Max = {max_values[column]}")
            print(bins)'''

            labels = range(0, intervals)


        # print(data[:, column])
        binned_data = pd.cut(data[:,column], bins=bins, labels=labels)
        resultArray.append(binned_data.codes)

        '''print(binned_data)
        print()
        print()'''
    resultArray = np.array(resultArray)
    resultArray = np.transpose(resultArray)
    return resultArray




if __name__ == '__main__':
    # dataset1-timeSeries_new

    print(binning("dataSets/test2", 5))
    # (18646, 6)



