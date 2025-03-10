#!/usr/bin/env pythin 3

import numpy as np
import pandas as pd

"""This module takes the last 10 rows of the columns High and Close and converts them to numpy.ndarray"""

from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df[['High', 'Close']].tail(10)
A = df[['High', 'Close']].tail(10).to_numpy()
print(A)
