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

raw_fileaddress = baseaddress + '/' + raw_filename
clean_fileaddress = baseaddress + '/' + clean_filename
temp_fileaddress = baseaddress + '/' + temp_filename

with open(raw_fileaddress, 'r') as fo:
    for line in fo:
        print line
        line = line.replace('{','')
        line = line.replace('}','')
        line = line.replace('\\','')
        line = line.replace('\"','')
        print line
        with open(clean_fileaddress, 'a') as fw:
            fw.write(line)
            # fw.write('\n')

print "Log Cleaning: Done"