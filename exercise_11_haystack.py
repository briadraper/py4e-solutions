"Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_140565.txt (There are 80 values and the sum ends with 458)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis."

https://www.py4e.com/tools/python-data/index.php?PHPSESSID=b34776b1bb7220a44fae8e5ad05b8981

.....

import re

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    exit()

numlist = list()
for line in fhand:
    line = line.rstrip()
    num = re.findall('([0-9]+)', line)    #extract any number from line
    for number in num:                    #convert items in list to floating point
        fnumber = float(number)                     
        numlist.append(fnumber)           #put numbers in list called "numlist"
print('Number of Values:', len(numlist))  #prints out a count of how many numbers we found
print('Sum:', sum(numlist))               #prints the total of all the values found
