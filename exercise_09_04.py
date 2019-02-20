“Exercise 4   Add code to the above program to figure out who has the most messages in the file.
After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Section ??) to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File not found: ', fname)
    exit()

emails = dict()
for line in fhand:
    if line.startswith ('From '):
        word = line.split()
        email = word[1]
        emails[email] = emails.get(email,0) + 1
largest = None
for key in emails:
    if largest is None or emails[key] > largest:
            largest = emails[key]
            sender = key
print(sender, largest)
