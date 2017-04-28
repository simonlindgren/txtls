#!/usr/bin/env python

"""
script: txt-joiner.py
author: Simon Lindgren
non-standard packages: PyPDF2
functionality: creates txt versions of all pdf files in the working directory
"""

import PyPDF2
import os

# read pdf names in this directory into a list
filelist = []
for file in os.listdir():
    if file.endswith(".pdf"):
        filelist.append(file)

print(filelist)

#iterate over the filelist
for f in filelist:
    pdfFileObj = open(f, 'rb') # open the pdf
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # read it as a pypdf2 object
    num_pages = pdfReader.numPages # get the number of pages

    text_file = open((f[:-4] + ".txt"), "w")  # create output txt file

    for p in range(num_pages): # iterate over the pages
        pageObj = pdfReader.getPage(p) # get the raw text content of the page
        text_file.write("\n" + (pageObj.extractText()) + "\n") # write it to the output file
        print("Processing file " + f[:-4] + ", page " + str(p+1)) # post progress info

print("Done.")