#!/usr/bin/env python

"""
script: dir-maker.py
author: Simon Lindgren
functionality: creates a set of empty directories from a list of directory names in a text file
"""

import os
dirs = open("dirs.txt", "r").readlines()
for dir in dirs:
	os.mkdir(dir)


