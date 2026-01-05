"""
Create a program to find and print all numbers from 0 to 1000 (both included),
that are divisible by 7 and whose digits
sum are divisible by 3.
For instance, 1512 is divisible by 7 and the sum of all its is digits (9) is divisible by 3.
Another example, 21 is divisible by 7, and the sum of its digits (3) is divisible by 3.
Example
If the exercise were to make the same computation but in the range(1500, 1700),
the solution should print:
"""
for num in range(0, 1001):
    if num%7==0:
        sum=0
        for i in str(num):
            sum+=int(i)
        if sum%3==0:
            print(num)








