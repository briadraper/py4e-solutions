“Exercise 1  
Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

fname = input('Enter a file name: ')
fhandle = open(fname)
words = dict()
ftext = fhandle.read()
wordlist = ftext.split()
for word in wordlist:
    words[word] = 0
    print(wordlist)
while True:
    check = input('Enter a word: ')
    if check in words:
        print('True')
    else:
        print('False')
        if check == 'I am done':
            break
input("\n\nPress Enter to exit")
