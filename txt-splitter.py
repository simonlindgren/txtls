#!/usr/bin/env python

"""
script: txt-splitter.py
author: Simon Lindgren
non-standard packages: -
functionality: splits a textfile into a zip archive containing one textfile per line in the original textfile
"""
import zipfile
zf = zipfile.ZipFile("splits.zip", "w", zipfile.ZIP_DEFLATED) # create the zipfile

count = 0                                                     # set up a counter for naming the txt files
with open('big.txt','r') as infile:
    for line in infile:                                       # iterate over the lines in the big txt file
        count +=1
        filename = (str(count) + '.txt')                      # generate the filename
        zf.writestr(str(filename), str(line))                 # write the line to the txt and put it in the zip
