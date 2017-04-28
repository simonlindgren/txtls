#!/usr/bin/env python

"""
script: txt-joiner.py
author: Simon Lindgren
non-standard packages: -
functionality: joins all txt files in a folder into one big txt file
"""

import glob
fs = glob.glob("*.txt")                                       # get a list of all files

with open("big.txt", "wb") as outfile:                             # create output file
    for f in fs:                                                   # iterate over the files
        with open(f, "rb") as infile:                              # open the file
            outfile.write(f.encode('ascii')+"\n".encode('ascii'))  # write the filename on one line
            outfile.write(infile.read()+"\n\n".encode('ascii'))    # write the file content
