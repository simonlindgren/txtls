#!/usr/bin/env python

"""
script: csv-linebreak-remover.py
author: Simon Lindgren
non-standard packages: –
functionality: removes linebreaks from within csv fields and writes a new csv
"""

import csv
import re

with open("0.csv", "r") as input, open("output.csv", "w") as output:

    writer = csv.writer(output, delimiter=";")

    for row in csv.reader(input):
        new_row = []
        for item in row:
            new_item = re.sub("\n", " ", item)
            new_row.append(new_item)
        writer.writerow(new_row)