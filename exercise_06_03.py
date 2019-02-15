“Exercise 3  
Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

def count(word):
    position = 0
    for letter in word:
        if letter == 'a':
            position = position + 1

word = 'banana'
print (count)
