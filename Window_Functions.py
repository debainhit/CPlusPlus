#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 22:45:12
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$


# --------------------------------------------------------------------------
# for working on numerical data, Pandas provide few variants like rolling,
# expanding and exponentially moving weights for window statistics. 
# Among these are sum, mean, median, variance, convariance, correlation, etc
# Windows functions are majority used to finding the trends within the data 
# graphically by smoothing the curve.If there is a lot of variantion in the 
# everyday data and a lot of data points are available, then taking the sample 
# and plotting is one method and applying the window computations and plotting 
# graph on the results is another methods. By these methods, we can smooth the curve
# or the trend
# --------------------------------------------------------------------------


import pandas as pd
import numpy as np
print "rolling mean()"

df = pd.DataFrame(np.random.randn(10, 4),
index = pd.date_range('1/1/2000', periods=10),
columns = ['A', 'B', 'C', 'D'])
print df.rolling(window=3).mean()

print "expanding() Function"

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df.expanding(min_periods=3).mean()

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df.ewm(com=0.5).mean()
