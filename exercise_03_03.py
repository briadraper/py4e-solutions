"Exercise 3   Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F

Enter score: 0.95
A

Enter score: perfect
Bad score

Enter score: 10.0
Bad score

Enter score: 0.75
C

Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for input.

”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

score = input('Enter a score grade: ')
fscore = float(score)
if fscore >= 1.0 :
    print('error')
elif fscore >= 0.9 :
    print('A')
elif fscore >= 0.8 :
    print ('B')
elif fscore >= 0.7 :
    print ('C')
elif fscore >= 0.6 :
    print ('D')
elif fscore < 0.6 :
    print ('F')
    print('bad score')
