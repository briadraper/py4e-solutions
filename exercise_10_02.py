“Exercise 2   This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.
Sample Execution:
python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

#This program counts the distribution of the hour of the day for each of the messages.
#You can pull the hour from the “From” line by finding the time string and then splitting
#that string into parts using the colon character. Once you have accumulated the counts for
#each hour, print out the counts, one per line, sorted by hour.

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File not found: ', fname)
    exit()
    
hours = dict()
for line in fhand:
    if line.startswith ('From ') :
        word = line.split()        #split each line that starts with 'From ' into words
        time = word[5]            #define the 5th word as time
        delimiter = ':'         #delimiter specifies the colon to be used as word boundaries
        time.split(delimiter)
        hour = time[:2]         #defines hour as the first 2 digits of time
        hours[hour] = hours.get(hour,0) + 1     #idiom that counts how often that hour appears
#print(hours)

t = list()
for key, val in list(hours.items()):
    t.append((key, val))
    
t.sort()

for key, val in t:
    print(key, val)




