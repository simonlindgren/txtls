#!/usr/bin/env python

"""
script: txt-csv.py
author: Simon Lindgren
non-standard packages: pandas
functionality: creates a csv file of all txt files in the working directory
"""

import glob
import pandas as pd

# get all filenames in the data subdir
fs = glob.glob('data/*.txt')

# create a dataframe with an empty column named 'text'
cols = ['text']
df = pd.DataFrame(columns = cols)

# iterate over all filenames
for f in fs:
    with open(f, "r") as file:  # open file
        d = file.read()         # read file contents
    df.loc[f[5:-4]] = [d]       # write filename (-5 first/4 last chars) as index, and file context to the 'text' column

df.index.name = 'file'          # set the header for the index column
df.to_csv('raw.csv', sep=',')   # save everything to a csv file