'''
A modules that test criterion from HW3

'''

import unittest

import numpy as np

import create_dataframe as cdf

class UnitTests(unittest.TestCase):
    '''
    Unit test for HW3
    '''

    def test_hw2(self):
        '''
        Unit test for HW3 question 1.
        checking on function test_create_dataframe.
        test_create_dataframe function conatains the following tests.
        check if the DataFrame contains only the columns that you specified as the second argument.
        check if the values in each column have the same python type.
        check if there are at least 10 rows in the DataFrame.
        The test_create_dataframe takes two input:
        A dataframe read from url and column names specified by users.
        Use create_dataframe from create_dataframe module to read in the url.
        column_names specify the intended names for each columns in dataframe.
        The function return True if meet all three creterion.
        '''
        data_frame = cdf.create_dataframe(
            "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
        )
        column_names = ['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']
        self.assertTrue(cdf.test_create_dataframe(data_frame, column_names))

    def test_column_type_match(self):
        '''
        Unit test for HW3 question 2 part 1
        Check that all columns have values of the corect type that the user specified.
        Use create_dataframe from create_dataframe module to read in the url
        '''
        data_frame = cdf.create_dataframe(
            "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
        )
        dtype_match = [data_frame.iloc[:, i].apply(type).unique()
                       for i in range(data_frame.shape[1])
                      ]
        dtype_match = np.concatenate(dtype_match, axis=0)
        self.assertTrue(np.array_str(dtype_match) ==
                        "[<class 'str'> <class 'float'> <class 'float'>]")

    def test_nan(self):
        '''
        Unit test for HW3 question 2 part 2
        Check for nan values.
        '''
        data_frame = cdf.create_dataframe(
            "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
        )
        self.assertTrue(data_frame.isnull().values.any())

    def test_row(self):
        '''
        Unit test for HW3 question 2 part 3
        Verify that the dataframe has at least one row.
        '''
        data_frame = cdf.create_dataframe(
            "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
        )
        self.assertGreater(len(data_frame.index), 1)

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
