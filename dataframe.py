#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-02 22:53:36
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit

# -------------------------------------------------------------------------
# pandas.DataFrame(data, index, columns, dtype, copy)
# para:
#      data: data takes various form like ndarray, series, map, list, dict, 
#      constant and also another DataFrame
#      List dict Series Numpy ndarrays Another DataFrame
#      index: for the row labels, the index to be used for the resulting frame 
#      is Optional Default np.arrange(n) if no index is passed
#      column: for column labels, the Optional default syntax is - np.arrage(n)
#      this is only true if no index is passed
#      dtype: data type of each column
#      copy: this command(or whatever it is) is used for copying of data, 
#      if the default is False
# -------------------------------------------------------------------------





import pandas as pd

print "Create an Empty DataFrame"
df = pd.DataFrame()
print df

print "Create a DataFrame from Lists"
data = [1, 2,  3, 4, 5]
df = pd.DataFrame(data)
print df

data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print df

df = pd.DataFrame(data, columns=['Name', 'Age'], dtype=float)
print df

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'], 'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print df
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'], 'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1', 'rank2', 'rank3', 'rank4'])
print df

print "Create a DataFrame from list of Dicts"
"the dictionary keys are by default taken as column names"

data = [{'a':1, 'b':2}, {'a':5, 'b':10, 'c':20}]
df = pd.DataFrame(data)
print df

df = pd.DataFrame(data, index=['first', 'second'])
print df

df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print df1
print 
print df2

print "Create a DataFrame from Dict of Series"

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df

# column selection, addtion, deletion 
print "column selection"
print df['one']

print "column addtion"
df['three']=pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print df

df['four']=df['one']+df['three']
print df

print "column deletion"
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)

del df['one']

print df

df.pop('two')
print df

# row selection, addtion, deletion


d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df
# selection by label
print df.loc['b']

# selection by integer location
print df.iloc[2]

# slice rows

print df[2:4]


df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print df
df = df.drop(0)
print df