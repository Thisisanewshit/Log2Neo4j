# -*- coding: UTF-8 -*-
'''
This is just a tester
Suppose, only care apiVersion, eventName, eventTime, userName currently
'''
import os
import pandas as pd
import numpy as np
from pandas import DataFrame

baseaddress = os.path.dirname(__file__)
raw_filename = 'downloaded_data_sample.txt'
clean_filename = 'clean_data_sample.txt'
temp_filename = 'temp_sample.txt'
raw_fileaddress = baseaddress + '/'+ raw_filename
clean_fileaddress = baseaddress + '/'+ clean_filename
temp_fileaddress = baseaddress + '/' + temp_filename

with open(clean_fileaddress, 'r') as fo:
    temp_data = fo.readlines()
    # print temp_data
    print temp_data[0]
    print temp_data[1]
    print temp_data[2]
    # for readline in temp_data:
    #     print readline


