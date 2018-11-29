# -*- coding: UTF-8 -*-
'''
Raw log data is in txt file. Each piece of log maybe in different log format( it means it contains different key words.
This script is designed to follow the steps shown as below:
    1. Store all kinds of files address
    2. Clean up the raw log data basically.
    3. Read the first line of log data, convert it into dataframe, pick the spec column we want.
            Suppose, only care apiVersion, eventName, eventTime, userName currently
    4. Save the first piece of dataframe as the base dataframe
    5. Read the next line of log data
    ......
    6. Save the final result into txt file.


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

combined_data = DataFrame()

with open(clean_fileaddress, 'r') as fo:
    readlines = fo.readlines()
    for readline in readlines:

        # print readline
        with open(temp_fileaddress, 'a') as fw:
            fw.truncate()
            fw.write(readline)

        #readline should be a file instead of a string
        data = pd.read_table(temp_fileaddress, sep=',', header=None, nrows=1)

        i = -1
        headers = []
        values = []


        for temp_data in data:
            i=i+1
            value = ''
            header = data[i].str.split(':')[0][0]
            if (len(data[i].str.split(':')[0]) == 1):
                value = 'NA'
            if (len(data[i].str.split(':')[0]) == 2):
                value = data[i].str.split(':')[0][1]
            if (len(data[i].str.split(':')[0]) >2):
                for j in range(1, len(data[i].str.split(':')[0])):
                    if j == 1:
                        value = value + data[i].str.split(':')[0][j]
                    else:
                        value = value +':'+ data[i].str.split(':')[0][j]
            headers.append(header)
            values.append(value)

        data = pd.DataFrame([values],columns =headers)

        # print data[0]['userName']
        # data_new = data[['userName','eventName']].copy()
        data_new = data[['eventName', 'eventTime','userIdentity','userName','serviceName']].copy()
        combined_data = combined_data.append(data_new, ignore_index=True)

print combined_data

combined_data.to_csv('Result.csv')