“Exercise 2   Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.”

Excerpt From: Charles R. Severance. “Python for Informatics: Exploring Information.” Apple Books. 

....

largest = None
smallest = None
while True :
    try :
        num = input('Enter a number: ')
        if num == 'done' :
            break
        print (num)
        fnum = float(num)
        if largest is None or largest < fnum:
            largest = fnum
        elif smallest is None or smallest > fnum:
            smallest = fnum
    except :
            print('Invalid input')

print ('Maximum is', largest)
print ('Minimum is', smallest)
