"""
A program to determine if a number is perfect.
"""

import math

#request and store user input
value = int(input("Enter your value: "))

#store sum of factors
total_sum = 1

#find factors of value
for x in range(2, 1 + int(math.sqrt(value))):
    if value % x == 0:

        total_sum = total_sum + x + value / x

#determine if value is a perfect number
if value > 1 and total_sum == value:
    print(str(value) + " is a perfect number.")
else:
    print(str(value) + " is not a perfect number.")
