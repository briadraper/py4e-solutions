“Exercise 1  
Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

def chop(x):
    del x[0]
    del x[-1]

def middle(x):
    return x[1:-1]

lst = [1,2,3,4,5]

newlst = middle(lst)
print(newlst)

chop(lst)
print(lst)
