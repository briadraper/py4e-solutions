“Exercise 1   Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

import re                                             #import regular expressions

fhand = open('mbox-short.txt')                        #open mbox-short.txt file
inp_exp = (input('Enter a regular expression: '))     #prompt for a regular expression using the set notation, "[^ ]", which  
count = 0                                              means match a character that is anything other that a space


for line in fhand:                                    #for each line in the file, strip the whitespace from the right side
    line = line.rstrip()
    if re.findall(inp_exp,line) != []:                #use findall to find the input and extract it from the line and count it 
        count += 1                                     if it is not [] (whitespace)

print('mbox-short.txt had', count, "lines that matched", inp_exp)
