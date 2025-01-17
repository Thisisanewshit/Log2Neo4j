# -*- coding: UTF-8 -*-
'''
Description: This script is aim to handle the action-trial log data from .txt to memory in specific data format.
Date: 20181127
Author: Shuai
Version: 0.00
'''

import sys
import os
import pandas as pd

mulu=os.path.dirname(__file__)
#日志文件存放路径
logdir="/home/test/python/log/log"
#存放统计所需的日志相关字段
logfile_format=os.path.join(mulu,"log.txt")

print "read from logfile \n"
for eachfile in os.listdir(logdir):
    logfile=os.path.join(logdir,eachfile)
    with open(logfile, 'r') as fo:
        for line in fo:
            spline=line.split()
            #过滤字段中异常部分
            if spline[6]=="-":
                pass
            elif spline[6]=="GET":
                pass
            elif spline[-1]=="-":
                pass
            else:
                with open(logfile_format, 'a') as fw:
                    fw.write(spline[6])
                    fw.write('\t')
                    fw.write(spline[-1])
                    fw.write('\n')
print "output panda"
#将统计的字段读入到dataframe中
reader=pd.read_table(logfile_format,sep='\t',engine='python',names=["interface","reponse_time"] ,header=None,iterator=True)
loop=True
chunksize=10000000
chunks=[]
while loop:
    try:
        chunk=reader.get_chunk(chunksize)
        chunks.append(chunk)
    except StopIteration:
        loop=False
        print "Iteration is stopped."

df=pd.concat(chunks)
#df=df.set_index("interface")
#df=df.drop(["GET","-"])

df_groupd=df.groupby('interface')
df_groupd_max=df_groupd.max()
df_groupd_min= df_groupd.min()
df_groupd_mean= df_groupd.mean()
df_groupd_size= df_groupd.size()

#print df_groupd_max
#print df_groupd_min
#print df_groupd_mean

df_ana=pd.concat([df_groupd_max,df_groupd_min,df_groupd_mean,df_groupd_size],axis=1,keys=["max","min","average","count"])
print "output excel"
df_ana.to_excel("test.xls")