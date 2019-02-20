“Exercise 2   Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

fname = input ('Enter a file name: ')
try:
    fhandle = open(fname)
except:
    print('File not found: ', fname)
    exit()

days = dict()                             #create a dictionary named "days"
for line in fhandle:                      
    if line.startswith ('From '):         #split each line in file and skip any line that does not start with 'From '
        word = line.split()               #split each word on each line that starts with 'From '
        day = word[2]                     #parse the 3rd word out
        days[day] = days.get(day,0) + 1   #count how many times the third word occurs
print(days)
