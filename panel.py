#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 15:47:32
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$




# ---------------------------------------------------------------
# pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)

# paras:
#       data: Data takes various form like ndarray, series, map, 
#       list, dict, constants and another DataFrame
#       items: axis = 0
#       major_axis: axis = 1
#       minor_axis: axis = 2
#       dtype = Data type of each column
#       copy = Copy data, Default, false
# ---------------------------------------------------------------

import pandas as pd
import numpy as np

print "Create Panel"
# from ndarrays, dict of DataFrames 
p = pd.Panel()
print p

data = np.random.rand(2, 4 ,5)
print data
p = pd.Panel(data)
print p

data = { 'Item1' : pd.DataFrame(np.random.randn(4, 3)),
         'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p

print "Selecting the Data from Panel"
#items, Major_axis, Minor_axis 

data = { 'Item1' : pd.DataFrame(np.random.randn(4, 3)),
         'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p['Item1']
print p.major_xs(1)
print p.minor_xs(1)
