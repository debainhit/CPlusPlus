#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 23:20:33
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$

# --------------------------------------------------------------------
# this functionality on Series and DataFrames is just a simple wrapper
# around the matplotlib libraries plot() method 
# if the index consists of dates, it calls gct().autofmt_xdate() to format
# the x-axis as shown in the above illustration
# --------------------------------------------------------------------


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), 
	index = pd.date_range('1/1/2000', periods =10),
	columns=list('ABCD'))
df.plot()

# --------------------------------------------------------------------------------
# we can plot one columns versus another using the x and y keywords
# Plotting methods allow a handful of plot styles other than the default line plot
# bar or barh for bar plot
# hist for histogram
# box for boxplot
# 'area' for area plots
# 'scatter' for scatter plots
# -----------------------------------------------------------------------------------