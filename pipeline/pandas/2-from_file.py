#!/usr/bin/env python3
import pandas as pd

#This module loads data from a file as a pd.DataFrame:


def from_file(filename, delimiter):
  """Loads data from a file as a pd.DataFrame"""
  return pd.read_csv(filename, delimiter=delimiter)