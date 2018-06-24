# 1. Reading the content of a file

## About files

There are two types of file depending on the data format they contain: [plain text](https://en.wikipedia.org/wiki/Plain_text) and [binary](https://en.wikipedia.org/wiki/Binary_file).

Files in plain text are intended for humans to edit them in an easy way. You can use any text editor to change their content. 

We will focus in plain text files in the following sections:

## 1.1. Reading a file line by line

In the [data](data/) folder there is a sample FASTA file. A FASTA file is a plain text file containing nucleotide or peptide sequences information. [Read More](https://en.wikipedia.org/wiki/FASTA_format)

### Source code:

File: [read_1.py](read_1.py)

```python
"""Reads a file and prints line by line its content"""

with open("data/sequences.fasta", "r") as input_file:
    for line in input_file:
        print line

```

### Output:

```bash
$ python read_1.py 
>seq0

FQTWEEFSRAAEKLYLADPMKVRVVLKYRHVDGNLCIKVTDDLVCLVYRTDQAQDVKKIEKF

>seq1

KYRTWEEFTRAAEKLYQADPMKVRVVLKYRHCDGNLCIKVTDDVVCLLYRTDQAQDVKKIEKFHSQLMRLME LKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM

>seq2

EEYQTWEEFARAAEKLYLTDPMKVRVVLKYRHCDGNLCMKVTDDAVCLQYKTDQAQDVKKVEKLHGK

>seq3

MYQVWEEFSRAVEKLYLTDPMKVRVVLKYRHCDGNLCIKVTDNSVCLQYKTDQAQDVK

>seq4

EEFSRAVEKLYLTDPMKVRVVLKYRHCDGNLCIKVTDNSVVSYEMRLFGVQKDNFALEHSLL

>seq5

SWEEFAKAAEVLYLEDPMKCRMCTKYRHVDHKLVVKLTDNHTVLKYVTDMAQDVKKIEKLTTLLMR

>seq6

FTNWEEFAKAAERLHSANPEKCRFVTKYNHTKGELVLKLTDDVVCLQYSTNQLQDVKKLEKLSSTLLRSI

>seq7

SWEEFVERSVQLFRGDPNATRYVMKYRHCEGKLVLKVTDDRECLKFKTDQAQDAKKMEKLNNIFF

>seq8

SWDEFVDRSVQLFRADPESTRYVMKYRHCDGKLVLKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM

>seq9

KNWEDFEIAAENMYMANPQNCRYTMKYVHSKGHILLKMSDNVKCVQYRAENMPDLKK

>seq10

FDSWDEFVSKSVELFRNHPDTTRYVVKYRHCEGKLVLKVTDNHECLKFKTDQAQDAKKMEK

```
