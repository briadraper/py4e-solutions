“Exercise 1   Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

name = input('Enter a file name: ')
try:
     fhand = open(fname)
except:
    print('File not found: ', fname)
    exit()

addresses = dict()
for line in fhand:
    if line.startswith ('From '):
        word = line.split()
        address = word[1]
        addresses[address] = addresses.get(address,0) + 1     #idiom
print(addresses)

t = list()        #Make an empty list
for key, val in list(addresses.items()):
    t.append((val, key))        #Add the tuples from the dict named "addresses" to the empty list with the order of value, key.

t.sort(reverse=True)        #Sort the list in reverse order from biggest value to smallest

for key, val in t[:1]:       #print only the person with the most commits
    print(val, key)
