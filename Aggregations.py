#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 23:03:26
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$

# ------------------------------------------------------------
# Once the rolling, expanding and ewm objects are created,
# several methods are available to perform aggregation on data
# ------------------------------------------------------------

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
	 index = pd.date_range("1/1/2000", periods=10),
	 columns = ['A', 'B', 'C', 'D'])
print df

print "Applying Aggregation on DataFrame"

# we can aggregate by passing a function to the entire DataFrame, or select a column 
# via the standard get item method

r = df.rolling(window=3, min_periods=1)
print r.aggregate(np.sum)


print "Apply Aggregation on a Single Column of a DataFrame"
print r['A'].aggregate(np.sum)

print "Apply Aggregation on Multiple Columns of a DataFrame"
print r[['A', 'B']].aggregate(np.sum)


print "Apply Multiple Funtions on a Single Columns of a DataFrame"
print r['A'].aggregate([np.sum, np.mean])

print "Apply Multiple Functions on Multiple Columns of a DataFrame"
print r[['A','B']].aggregate([np.sum,np.mean])

print "Apply Different Functions to Different Columns of a Dataframe"
print r.aggregate({'A':np.sum, 'B':np.mean})