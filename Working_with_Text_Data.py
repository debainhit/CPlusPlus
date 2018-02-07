#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-05 21:03:00
# @Author  : debainhit (18068920049@163.com)
# @Link    : https://github.com/debainhit
# @Version : $Id$

# ----------------------------------------------------------
# string operations with our basic Series/Index.
# apply these string functions on the DataFrame
# Most importantly, these functions ignore(or exclude)
# missing/NaN values
# all of these methods work with Python string functions 
# convert the Series Object to String Object and then perform
# the operations
# ----------------------------------------------------------


import pandas as pd
import numpy as np
s = pd.Series(['Tom ', '  William Rick', 'John', 'Aelber@t', np.nan, '1234', 'SteveSmith'])
print s
print s.str.lower()
print s.str.upper()
print s.str.len()
print s.str.strip()
print s.str.split('')
print s.str.cat(sep='_')
print s.str.get_dummies()
print s.str.contains(' ')
print s.str.replace('@', '$')
print s.str.repeat(2)
print s.str.count('m')
print s.str.startswith('T')
print s.str.endswith('t')
print s.str.find('e')
print s.str.findall('e')
print s.str.swapcase()
print s.str.islower()