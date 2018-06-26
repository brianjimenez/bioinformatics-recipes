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

## 1.2. Reading a file line by line and removing newline

To get rid of the newline character, we will use the function from string `rstrip(s)`. This functions removes the string `s` from the **right** part of the string (the reason why the function is called r-strip).

Newline character is OS dependent, that is, in GNU/Linux OS is used the `'\n'` character, but it is different in Windows. To avoid this problem of reading files with different newline characters, we will use the handy  `os.linesep` abstraction from the `os` Python library. This library, `os`, provides many more functions OS-dependent such as creating folders, traversing file-system paths and so on.

### Source code:

File: [read_2.py](read_2.py)

```python
"""Reads a file and prints line by line its content"""

import os


with open("data/sequences.fasta", "r") as input_file:
    for line in input_file:
        line = line.rstrip(os.linesep)
        print line

```

### Output:

```bash
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

## 1.3. Reading a file all lines at the same time

We could be interested in reading all the lines from a file at once and then process them afterwards:

### Source code:

File: [read_3.py](read_3.py)

```python
"""Reads a file at once and prints line by line its content"""

import os


with open("data/sequences.fasta", "r") as input_file:
    lines = input_file.readlines()
    for line in lines:
        line = line.rstrip(os.linesep)
        print line

```

The output will be the same as in the previous section.

If we slightly modify the previous code in order to print `lines` we will observe:

```python
"""Reads a file at once and prints line by line its content"""

import os


with open("data/sequences.fasta", "r") as input_file:
    lines = input_file.readlines()
    print lines
    for line in lines:
        line = line.rstrip(os.linesep)

```

The variable `lines` is a list of strings:

```bash
['>seq0\n', 'FQTWEEFSRAAEKLYLADPMKVRVVLKYRHVDGNLCIKVTDDLVCLVYRTDQAQDVKKIEKF\n', 
'>seq1\n', 
'KYRTWEEFTRAAEKLYQADPMKVRVVLKYRHCDGNLCIKVTDDVVCLLYRTDQAQDVKKIEKFHSQLMRLME LKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM\n', 
'>seq2\n', 
'EEYQTWEEFARAAEKLYLTDPMKVRVVLKYRHCDGNLCMKVTDDAVCLQYKTDQAQDVKKVEKLHGK\n', 
'>seq3\n', 'MYQVWEEFSRAVEKLYLTDPMKVRVVLKYRHCDGNLCIKVTDNSVCLQYKTDQAQDVK\n', 
'>seq4\n', 'EEFSRAVEKLYLTDPMKVRVVLKYRHCDGNLCIKVTDNSVVSYEMRLFGVQKDNFALEHSLL\n', 
'>seq5\n', 'SWEEFAKAAEVLYLEDPMKCRMCTKYRHVDHKLVVKLTDNHTVLKYVTDMAQDVKKIEKLTTLLMR\n', 
'>seq6\n', 'FTNWEEFAKAAERLHSANPEKCRFVTKYNHTKGELVLKLTDDVVCLQYSTNQLQDVKKLEKLSSTLLRSI\n',
'>seq7\n', 'SWEEFVERSVQLFRGDPNATRYVMKYRHCEGKLVLKVTDDRECLKFKTDQAQDAKKMEKLNNIFF\n', 
'>seq8\n', 'SWDEFVDRSVQLFRADPESTRYVMKYRHCDGKLVLKVTDNKECLKFKTDQAQEAKKMEKLNNIFFTLM\n', 
'>seq9\n', 'KNWEDFEIAAENMYMANPQNCRYTMKYVHSKGHILLKMSDNVKCVQYRAENMPDLKK\n', 
'>seq10\n', 'FDSWDEFVSKSVELFRNHPDTTRYVVKYRHCEGKLVLKVTDNHECLKFKTDQAQDAKKMEK\n']
```

This option of reading all the file content at once might not be the best option if the file size is huge (in the order of several MB or bigger) as this will be stored in physical memory during the execution of the code.