#!/usr/bin/env python3

import numpy as np
import pandas as pd

"""This module renames a column, converts the timestamp values to datatime values and displays only the datetime and close columns"""


df = pd.DataFrame({'Timestamp':["22:02:00", "22:03:00","22:04:00","22:05:00", "22:06:00"],
                  'Close': [4006.01, 4006.01, 4006.01, 4006.05, 4006.06]})

#Rename Timestamp to Datetime
df.rename(columns={'Timestamp': 'Datetime'}, inplace=True)
  
df = df[['Datetime', 'Close']]
print(df)