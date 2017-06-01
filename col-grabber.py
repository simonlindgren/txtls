#!/usr/bin/env python

"""
script: col-grabber.py
author: Simon Lindgren
non-standard packages: pandas
functionality: creates a txt file with the contents of a selected csv file column
"""

# Move to your data directory
import os
path = './data/'
os.chdir(path)

# Loop through the csv files
import pandas as pd

for file in os.listdir(): # for each file in the directory
    if file.endswith(".csv"): # if it has the csv extension
        f = open(file, 'r') # open it
        dataframe = pd.read_csv(f, sep=";") # into a dataframe

        #headers = dataframe.dtypes.index # view the column names if needed
        #print(headers)

        small_frame = dataframe[['target']] # extract the column with the name 'target' into a smaller dataframe
        small_frame.to_csv((file[:-4]+'.txt'), header=None, index=None, sep=' ', mode='a') # write it to a file
        f.close() # close the file and return to the top of the loop
