“Exercise 5   Take the following Python code that stores a string:‘

str = ’X-DSPAM-Confidence:  0.8475’
Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

str = 'X=DSPAM-Confidence: 0.8475'

ipos = str-find(':')
piece = str[ipos+2:]
value = float(piece)
print(value)
