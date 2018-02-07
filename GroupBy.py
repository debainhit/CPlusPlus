#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-07 16:12:51
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$

# ---------------------------------------------------------------
# any groupby operation involves one of the following operation
# on the original object. They are

# Splitting the Object
# Applying a function
# Combining the results

# In many situations, we split the data into sets and we apply some 
# functionality on each subset. In the apply functionality, we can 
# perform the following operations-
# Aggregation- computing a summary statistic
# Transformation- perform some group-specific operation
# Filtration- discarding the data with some conditon
# ---------------------------------------------------------------

import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)
print df


print "Split Data into Gruoup"

print df.groupby("Team")
print df.groupby("Team").groups

print "Group by with multiple columns"
print df.groupby(["Team","Year"]).groups



# By default, the groupby object has the same label name as the group name
grouped = df.groupby("Year")
for name, group in grouped:
	print name,group

print grouped.get_group(2014)

# An aggreagated function returns a single aggregated value for each group
# Once the group by object is created, several aggregation operations can be 
# performed on the grouped data
print "Aggregations"

print grouped['Points'].agg(np.mean)

print "The size of each group by applying the size() function"

grouped = df.groupby('Team')
print grouped.agg(np.size)

print "Applying Multiple Aggregation Function at Once"
# With grouped Series, pass a list or dict of functions to do aggregation with,
# and generate DateFrame as output

grouped = df.groupby('Team')
print grouped['Points'].agg([np.sum, np.mean, np.std])

print "Transformation"
score = lambda x: (x - x.mean()) / x.std()*10
print grouped.transform(score)
for name, group in grouped:
	print name,group


print "Filtration"

# Filtration filters the data on a defined citeria and returns the subset of 
# data. The filter() function is used to filter the data.

print df.groupby("Team").groups
print df.groupby('Team').filter(lambda x: len(x) >=3)