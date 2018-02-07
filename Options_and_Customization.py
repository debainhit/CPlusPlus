#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 21:21:24
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$


# -----------------------------------------------
# API to customize some aspects of its behavior,
# display is being mostly used
# get_option()
# set_option()
# reset_option()
# describe_option()
# option_context()
# -----------------------------------------------





import pandas as pd
print "get_option(param)"
print pd.get_option("display.max_rows")
print pd.get_option("display.max_columns")

print "set_option(param, value)"
pd.set_option("display.max_rows", 80)
print pd.get_option("display.max_rows")

pd.reset_option("display.max_rows")
print pd.get_option("display.max_rows")

print "describe_option(param)"
pd.describe_option("display.max_rows")

with pd.option_context("display.max_rows", 10):
	print pd.get_option("display.max_rows")
print(pd.get_option("display.max_rows"))