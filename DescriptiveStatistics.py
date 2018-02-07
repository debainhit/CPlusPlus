#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 16:12:48
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$

import pandas as pd
import numpy as np

#Create a Dictionary of series (columns)
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFram 
df = pd.DataFrame(d)
print df
print df.sum()
print df.mean()
print df.std()
print df.prod(1)

# object - Summarizes String columns
# nunmber - Summarizes Numberic columns
# all - Summarizes all columns together


print df.describe(include=['object'])
print df.describe(include=['all'])
