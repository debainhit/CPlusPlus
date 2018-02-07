#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 18:42:09
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$




# definition:
#         the behavior of the basic iteration over Pandas objects depends on the type.
#         When iterating over a Series, it is regarded as array-like, and basic iteration
#         produces the vaules. 
#         Other data structures, like DataFrame and Panel, follow the dict-like convention 
#         of iterating over the keys of the objects
# Operations:
#          To iterate over the rows of the DataFrame, we can use the following functions
#          iteritems() - to iterate over the (key, value) pairs
#          iterrows() - iterate over the rows as (index, series) pairs
#          itertuples() - iterate over the rows as namedtuples
# Iterat congnition:
#          do not try to modify any object while iterating. Iterating is meant for reading 
#          and the iterator returns a copy of the original object(a view), thus the changes 
#          will not reflect on the original object


import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
	'A': pd.date_range(start='2016-01-01', periods=N, freq='D'),
	'x': np.linspace(0, stop=N-1, num=N),
	'y': np.random.randn(N),
	'C': np.random.choice(['Low', 'Medium', 'High'], N),
	'D': np.random.normal(100, 10, size=(N)).tolist()
	})

print df
for col in df:
	print col


print "iteritems()"
# each column is iterated separately as a key-value pair in a Series
df = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])
for key,value in df.iteritems():
	print key, value
print "iterrows()"

# Because iterrows() iterate over the rows, it doesn't preserve the data type across the row,
# 0, 1, 2 are the row indices and col1, col2, col3 are the column indices.

for row_index, row in df.iterrows():
    print row_index,row

print "itertuples()"
for row in df.itertuples():
	print row
