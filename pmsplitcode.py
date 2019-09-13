#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 06:52:30 2019

@author: YUN
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns


data = pd.read_csv('/Users/YUN/desktop/Work/PBL/dataset.csv')
pm = pd.read_csv('/Users/YUN/desktop/Work/PBL/PM Time.csv')
pm = pm.iloc[:,:2]

data = data.reset_index(drop = True) 
pm = pm.reset_index(drop = True)

pm['module'] = np.nan 
pm['pm_period'] = np.nan

data = data.rename(columns = {'Module': 'module'})


for i in range(len(pm)): 
    pm['module'][i], pm['pm_period'][i] = pm['count'][i].split('-')

module_count = list(set(list(pm['module'])))

module_count = [int(i) for i in module_count]

module = []

for i in range(len(module_count)): 
    module.append(i)
for i in range(len(module)): 
    module[i] = pm.groupby('module').get_group(i+1)
for i in range(len(module)): 
    module[i] = module[i].reset_index(drop = True)
    
data['PM_STATUS'] = np.nan

data = data.sort_values(by='Time', ascending=True)

for i in range(len(data)):
    a = data['module'][i]  
    
    pm_c = 0  
    while True: 
        if data['Time'][i] < module[a-1]['pm'][pm_c]: 
            pm_c += 1 
            break 
        else: 
            if pm_c < (len(module[a-1])-1): 
                pm_c += 1 
            else: 
                pm_c += 1 
                break 
    
    
    data['PM_STATUS'][i] = pm_c

module2=data[data['module']==2]

data.to_csv("dataset2.csv", na_rep='NaN', columns=None, header=data.columns, index=False)

data2 = pd.read_csv('/Users/YUN/downloads/dataset2.csv')