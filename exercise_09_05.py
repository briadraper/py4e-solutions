“Exercise 5   This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}”

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
        line = line.split()
        email = line[1]
        email = email.split('@')
        domain = email[1]
        emails[domain] = emails.get(domain,0) + 1     #idiom: retrieve/create/update counter
print(emails)
