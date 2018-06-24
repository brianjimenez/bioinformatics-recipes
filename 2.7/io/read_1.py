"""Reads a file and prints line by line its content"""

with open("data/sequences.fasta", "r") as input_file:
    for line in input_file:
        print line

