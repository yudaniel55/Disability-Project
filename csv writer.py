# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:35:05 2018

@author: Compaq
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import glob

files = glob.glob('ss*')
excel = pd.read_excel('Dictionaries.xlsx',sheetname=None,index_col=0,usecols=[1,2])

# load only the desired columns in the data files
column_list = list(excel['Column Code'].index)
data = pd.DataFrame()
x=0
for i in files:
    z=pd.read_csv(files[x],usecols=column_list,nrows=10000)
    print(z.head())
    z.to_csv('trunc'+files[x])
    x+=1



 
