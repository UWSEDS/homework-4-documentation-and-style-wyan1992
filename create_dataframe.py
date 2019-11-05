'''
A modules that include reading data from url and test three criterion from HW2

'''

import pandas as pd


def create_dataframe(url):
    '''
    A simple function to read in data from url
    take an url as input
    '''
    data = pd.read_csv(url)
    return data

def test_create_dataframe(data_frame, column_names):
    '''
    test function that takes as input: (a) a pandas DataFrame and (b) a list of column names.
    The function returns True if the following conditions hold:
    1. The DataFrame contains only the columns that you specified as the second argument.
    2. The values in each column have the same python type
    3. There are at least 10 rows in the DataFrame.
    '''
    if list(data_frame) != column_names:
        raise TypeError("Column name does not match")
    dtype_count = [data_frame.iloc[:, i].apply(type).nunique() for i in range(data_frame.shape[1])]
    if dtype_count != [1] * len(data_frame.columns):
        raise TypeError("Values in one or more column do not have the same python type")
    if len(data_frame.index) < 10:
        raise TypeError("There are less than 10 rows in dataframe")
    return True
