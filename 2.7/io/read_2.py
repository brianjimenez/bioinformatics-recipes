"""Reads a file and prints line by line its content"""

import os


with open("data/sequences.fasta", "r") as input_file:
    for line in input_file:
        line = line.rstrip(os.linesep)
        print line

