#!/usr/bin/env python

"""
script: dir-maker.py
author: Simon Lindgren
functionality: creates a set of empty directories from a list of directory names in a text file
"""

import os
dirs = open("dirs.txt", "r").readlines()
dirs = set(dirs) # remove duplicates from dir list
for dir in dirs:
	if not os.path.exists((dir).strip()):
		os.mkdir(dir.strip())
