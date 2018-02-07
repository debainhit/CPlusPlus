#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 17:03:04
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$

# ------------------------------------------------------------------

# to apply your own or another library's functions to Pandas objects.
# you should be aware of the three important methods the methods have 
# been discussed below. The appropriate method to use depends on whether 
# your functions expects to operate on entire DataFrame, row or column-wise,
# or element wise.
#          Table wise Function Application: pipe()
#          Row or Column Wise Function Application: apply()
#          Element wise Function Application: applymap()
# ------------------------------------------------------------------




import pandas as pd
import numpy as np

def adder(ele1, ele2):
	return ele1+ele2


df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print df
# create a new datafram
df_new = df.pipe(adder, 2)
print df_new
print df.apply(np.mean)

print "Row or Column Wise Function Application"

print df.apply(np.mean)
print df.apply(np.mean,axis=1)

df_new = df.apply(lambda x: x.max() - x.min())
print df_new


print "Element Wise Function Application"

print df['col1'].map(lambda x: x*100)
