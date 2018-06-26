"""Reads a file at once and prints line by line its content"""

import os


with open("data/sequences.fasta", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        line = line.rstrip(os.linesep)
        print line

