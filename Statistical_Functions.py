#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 22:34:56
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$


# --------------------------------------------------------------------------------
# Statistical methods help in the understanding and analyzing the behavior of data
# Pandas objects
# --------------------------------------------------------------------------------



import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4, 5, 4])
print s.pct_change()

df = pd.DataFrame(np.random.randn(5, 10))
print df.pct_change()
print df.pct_change(axis=1)

print "Convariance"
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print s1.cov(s2)

frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print frame['a'].cov(frame['b'])
print frame.cov()