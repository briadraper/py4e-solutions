“Exercise 3   Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages.”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

import string
fname = input('Enter a file name: ')
try:
    if len(fname) < 1 : fname = 'clown.txt'                     #shortcut to clown.txt file. Otherwise, type in a file name
    fhand = open(fname)
except:
    print('File not found: ', fname)
    exit()

letters = dict()                                                            #create dictionary named "letters"
for line in fhand:                                                          #for each line in the file
    line = line.translate(str.maketrans('', '', string.punctuation))        #syntax(fromstr, tostr, deletestr). fromstr and     
                                                                             tostr are null. deletestr is defined to delete all 
                                                                             punctuation.
    line = line.translate(str.maketrans('', '', string.digits))             #deletes all digits. See above syntax description.
    line = line.replace(' ', '')                                            #removes all spaces between words
    line = line.strip()                                     #removes all white space on the left and right sides of each line
    line = line.lower()                                                     #makes all letters lowercase
    t = line.split                                                          #splits each line into words
    for t in line:           
        word = list(t)                                                      #makes a list of words
        for letter in word:
            letters[letter] = letters.get(letter,0) + 1         #idiom: for all letters in each word, get letter and count it
print(letters)

abc = list()                                                                #makes a list
for key, val in list(letters.items()):
    abc.append((val, key))                                    #puts the tuple(letter, count) in the list in pairs (value first)

abc.sort(reverse=True)                                                      #sorts the list in reverse order of value

for key, val in abc:
    print(val, key)                                                         #prints the list with the order val, key
