#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 17:59:53
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$


# ----------------------------------------------------------------------
# Definition:
#     Reindexing changes the row labels and column labels of a DataFrame
#     To reindex means to confirm the data to match a given set of labels 
#     along a particular axis
# Operations:
#     Reorder the exisiting data to match a new set of labels
#     Insert missing value (NA) markers in label location where no data 
#     for the label existed
# ----------------------------------------------------------------------

import pandas as pd
import numpy as np

N = 20

df = pd.DataFrame({
	'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
	'x': np.linspace(0, stop=N-1, num=N),
	'y': np.random.randn(N),
	'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
	'D': np.random.normal(100, 10, size=(N)).tolist()
})

print df
#reindex the DataFrame
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])

print df_reindexed


print "Reinde to Align with Other Objects"

#You may wish to take an object and reindex its axes to be labeled the same as another object
#Consider the following example to understand the same

df1 = pd.DataFrame(np.random.randn(10, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])

# df1 = df1.reindex_like(df2)
# print df1

print "Fillong while Reindexing"

print df2.reindex_like(df1)

#Now Fill the NAN's with preceding Values
print "Data Frame with Forward Fill:"
print df2.reindex_like(df1, method='ffill')


print "Limit on Filling while Reindexing"
print df2.reindex_like(df1, method='ffill', limit=1)

print "Renaming"

df1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
print df1

print "After renaming the rows and columns"
print df1.rename(columns={'col1':'c1', 'col2':'c2'},
index = {0: 'apple',  1: 'banana', 2: 'durian'})

