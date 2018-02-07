#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 19:36:50
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$


# -----------------------------
# Sorting:
#         By label
#         By Actual Value     
# -----------------------------
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])
print unsorted_df

print "By Label"

sorted_df=unsorted_df.sort_index()
print sorted_df

print "Order of Sorting"

sorted_df=unsorted_df.sort_index(ascending=False)
print sorted_df

print "Sort the Columns"

sorted_df=unsorted_df.sort_index(axis=1)
print sorted_df

print "By Value"

unsorted_df = pd.DataFrame({ 'col1':[2, 1, 1, 1], 'col2':[1, 3, 2, 4]})
sorted_df = unsorted_df.sort_values(by='col1')
print sorted_df

sorted_df = unsorted_df.sort_values(by=['col1', 'col2'])
print sorted_df

sorted_df = unsorted_df.sort_values(by='col1', kind='mergesort')
print sorted_df
