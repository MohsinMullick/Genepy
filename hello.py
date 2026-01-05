"""Hello World!"""
from django.contrib.admin.templatetags.admin_list import results

print("Hello World!")
#print 42
print("42")
#Number of seconds in a year
print(24*60*60*365)
#Write a Python script that prints the result for 8958937768937 divided by 2851718461558.
print(8958937768937/2851718461558)

#Characters counting
whetting_your_appetite = """Python is an easy to learn, powerful
programming language. It has efficient high-level data structures and
a simple but effective approach to object-oriented
programming. Python’s elegant syntax and dynamic typing, together with
its interpreted nature, make it an ideal language for scripting and
rapid application development in many areas on most platforms."""
print(len(whetting_your_appetite))


"""Fix the indentation
the given snippet, there's a bug: there's no indentation.
Your goal is to fix it (by just adding 4 spaces at the right place).
The code should display:
Gonna knock three times:
*knock*
*knock*
*knock*
- Who's there?
"""
print("Gonna knock three times:")
for i in range(3):
    print("*knock*")
print("- Who's there?")

#Square numbers

for i in range(10):
    print(i**2)
"""Power of Two 
Print the 10 first powers of two, one per line. (beware: not the first squares)
Start at 0, so the first power of two is 20 (which happen to be one), followed by 
21, 22, and so on up to 29.
As a reminder, the power operator in Python is written **, so:"""
n1=2
for i in range(0,10):
    print(n1**i)

"""Write a script that print the factorial of 27.
Use the factorial function from the math module.
Advice
You'll need to import the math module:
import math
"""
import math
print(math.factorial(27))

#Comparisions bigger numbers
"""Find the biggest value in a given list.
Try it by using only a temporary variable, a for loop, and an if to compare the values."""
the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]
max_num=0
for i in the_list:
    if i>max_num:
        max_num=i
print(max_num)

#!/usr/bin/env python3

whetting_your_appetite = ("Python is an easy to learn, powerful programming language."
                          " It has efficient high level data structures and a simple but"
                          " effective approach to object oriented programming. "
                          "This tutorial introduces the reader informally to the "
                          "basic concepts and features of the Python language and system."
                          " For a description of standard objects and modules...")

# Enter your code below:
words = whetting_your_appetite.split()
print(len(words))

#Fix is Anagram
"""
I've written a function called is_anagram.
This function takes two parameters:
left: it expects just one word, as a Python str.
right: it also expects just one word, as a Python str.
the function should return True if the two words are anagrams, False otherwise.
Sadly there's a small error in my implementation (try to submit it if you don't catch it),
can you fix it?
Just in case you messed with the code too much and want to start fresh, here it is:
def is_anagram(left, right):
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters = right_letters
"""
def is_anagram(left, right):
    # Normalize case and remove spaces
    left = left.replace(" ", "").lower()
    right = right.replace(" ", "").lower()
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters == right_letters

"""
Write a function computing the perimeter of a circle given its radius.
First read the function tutorial.
Your function should be named circle_perimeter(radius), where the radius parameter is the radius
of a circle.
Your function should return the perimeter of a circle of the given radius.
To test it, we will import your function and try it with different values, such as:
"""

import math
def circle_perimeter(radius):
    return 2*math.pi*radius
circle_perimeter(1)
circle_perimeter(10)
circle_perimeter(100)

#print even numbers
def print_even_numbers(start,stop):
    for i in range(start,stop):
        if i%2==0:
            print(i)

#Sum of even numbers 100
count=0
for i in range(0,101):
    if i%2==0:
        count+=i
print(count)

#Multiples of 3 and 5
"""
Write a program that finds the sum of all natural numbers below 1000 (< 1000) 
that are multiples of 3 or 5, and prints it.
If we list all the natural numbers below 20 (<20)
that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, 18. 
The sum of these multiples is 78.
Note that 15 is only counted once.
"""
Total=0
for i in range(0,1000):
    if i%3==0 or i%5==0:
        Total+=i
print(Total)
#Celcius to Fahrenheit and celsius to fahrenheit
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9
def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32













