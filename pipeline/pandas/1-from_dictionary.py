#!/usr/bin/env python3
import numpy as np
import pandas as pd


"""Creating a pd.DataFrame from a dictionary"""
d = {
  'First': ['0.0','0.5','1.0','1.5'],
  'Second':['one', 'two', 'three', 'four']}

#Customizing Indexing
df = pd.DataFrame(d, index = ['A', 'B', 'C', 'D'])
print(df)