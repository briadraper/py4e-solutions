“Exercise 2   Write a program to look for lines of the form
New Revision: 39772

and extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average.

Enter file:mbox.txt 
38549.7949721

Enter file:mbox-short.txt
39756.9259259
”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

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
    num = re.findall('^New Revision: ([0-9]+)', line) #find/extract the number in the line that is preceded by "New Revision: "
    if len(num) > 0:                                  #if the number of items in the list(x) is not equal to 1, continue.
        for number in num:                              #or if there is a match, then drop it down
            fnumber = float(number)                   #convert the match to a number
        numlist.append(fnumber)                       #put the number in the list called numlist
        average = sum(numlist) / len(numlist)         #calculate the average of the numbers
print('Average:', average)
