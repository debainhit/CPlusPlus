#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 21:58:26
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$


# ---------------------------------------------------------------------------------------------
# how to slice and dice the date and generally get the subset of the pandas object
# The Python and Numpy indexing "[ ]" and attribute operator "." provide quick and easy access
# to Pandas data structure across a wide range of use cases. However, since the type of the data
# to be accesssed isn't know in advance, directly using standard operators has some optimization limits.
# for production code, we recommend that you take advantange of the optimized pandas data access methods
# explained in this chapter
# Pandas now supports three types of Multi-axes indexing; the three types are mentioned in the 
# following table-
# Indexing                     Description
# .loc()                   Label based 
# .iloc()                  Integer based
# .ix()                    Both Label and Integer based
# ---------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
columns = ['A', 'B', 'C', 'D'])


# select all rows for a specific column
print df.loc[:,'A']
# select all rows for multiple columns, say list[]
print df.loc[:, ['A','C']]
# select few rows for multiple columns, say list[]
print df.loc[['a', 'b', 'c', 'f', 'h'], ['A', 'C']]
# select range of rows for all columns
print df.loc['a':'h']
print df.loc['a']>0

print "iloc()"
# select all rows for a specific column
print df.iloc[:4]

# Integer slicing 
print df.iloc[:4]
print df.iloc[1:5, 2:4]

# Slicing through list of values
print df.iloc[[1, 3, 5], [1, 3]]
print df.iloc[1:3, :]
print df.iloc[:, 1:3]



print ".ix()"
# Integer slicing
print df.ix[:4]
print df.ix[:, 'A']


print "Use of Notations"
# Getting values from the Pandas object with Multi-axes indexing uses the following notation
# Series s.loc[indexer] Scalar value
# DataFrame df.loc[row_index, col_index] Series object
# Panel p.loc[item_index, major_index, minor_index] 

print "directly operators on DataFrame"
print df['A']
print df[['A', 'B']]
print df[2:4]

print "attribute access"

print df.A