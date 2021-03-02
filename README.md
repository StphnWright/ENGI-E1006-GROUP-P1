**ENGI E1006 - Intro to Computing for Engineers & Applied Scientists**

**Group Exercise Set 1**

Due: Wed February 3 11:59pm, New York time (ET / GMT-5) 

Please ask the instructor and CAs/TAs for help if you get stuck. 

Some material needed for this exercise set will not be discussed until the week of January 25.

Use input() to read user input and print() to print results. Remember to convert the user input 
to integers where necessary. Do not use Python modules other than those explicitly mentioned. 

Unlike the take-home projects, the group exercises are intended to be worked on your assigned groups
on repl.it. You can work with your group during Thursday class and you are welcome to continue in your
own time. If you do not complete these problems during class, you must complete them at another time.

Groups should upload a single version of their solutions. 

Comments in Python start with with a "# ..." 

Upload the following four files to Courseworks:

    problem1.py
    problem2.py
    problem3.py
    problem4.py

Important: If you re-submit your assignment you need to re-upload all files, even if you changed just 
one of them. Otherwise, any files you uploaded previously will be lost if you submit a second time. 

**Problem 1 (25 pts) - Paint Calculator**

Write a program that estimates how much paint is needed to paint a rectangular room. Assume that the room
has no windows and no doors, and that the floor does not have to be painted. Your program should read in
the height, width, and length dimensions of the room in centimeters (cm). It should then print out the amount
of paint needed in liters. Assume that 2.5 liters are needed to paint a surface area of 10 m2.

Save your program in a file problem1.py.

**Problem 2 (25 pts) - 24-hour Clock**

A day has 86,400 secs (24 * 60 * 60). Given a number in the range
1 to 86,400 (inclusive), output the corresponding time as hours, minutes and seconds in a 24-hour clock format.

For example 70,000 seconds is "19 hours, 26 minutes, and 40 seconds". Your program should ask the user to type
in a number of seconds and then print the time. Make sure you correctly format the case where one or more of the
values is 1, for example "1 hour, 1 minute, and 1 second".

Save your program in a file problem2.py.

**Problem 3 (25 pts) - Perfect Numbers**

A number is perfect if it is equal to the sum of its factors (except itself, but including 1). For example,
28 (with factors 1,2,4,7,14) is perfect because 28 = 1+2+4+7+14. Write a Python program to determine if a
number is perfect. Try to make your program as efficient as possible by reducing the number of tests required.

Save your program in a file problem3.py.

**Problem 4 (25 pts) - k-smallest numbers**

Write a Python program to produce a list of the k-smallest numbers in a list of numbers. 

    For example, if

    li = [1,2,5,4,3,2]
    k=3

The output should be a list [1,2,2]

Discuss the algorithm for doing this first (possibly using pen and paper) before starting to program. Do NOT sort
the list for this problem (e.g. do not use the list.sort() method). Your program may contain specific values for
li and k hard-coded in the code, but should still work if these values are changed in the file.

Save your program in a file problem4.py.
