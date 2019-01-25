Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

We won't worry about making sure our pay has exactly two digits after the decimal place for now. if you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.

Python for Everybody: Exploring Data with Python 3

By Charles Severance

....

Hours = input('Enter Hours: ')
Rate = input('Enter Rate: ')
Pay = float(Hours) * float(Rate)
print('Pay:', Pay)

