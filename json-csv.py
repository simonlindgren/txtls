#!/usr/bin/env python

"""
script: json-csv.py
author: Simon Lindgren
non-standard packages: pandas
functionality: creates a csv file from a json file
"""

# Read JSON to Pandas
import pandas as pd
file = "tweets.json"
f = open(file, 'r')
df = pd.read_json(f)

df = df.replace('\n','', regex=True) # remove newlines in dataframe

df.to_csv("tweets.csv", sep = ";") # write csv