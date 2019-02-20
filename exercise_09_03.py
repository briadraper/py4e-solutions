“Exercise 3   Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3, 
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1, 
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3, 
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1, 
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2, 
'ray@media.berkeley.edu': 1}”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File not found: ', fname)
    exit()

addresses = dict()                      #create a dictionary named "addresses"
for line in fhand:                    
    if line.startswith ('From '):       #split each line in file that starts with 'From '
        word = line.split()             #split the words in each line that start with 'From '
        address = word[1]               #pull out the second word in each line
        addresses[address] = addresses.get(address,0) + 1       #count how many times the second word appears
print(addresses)
