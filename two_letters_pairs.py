"""
Provide a script printing every possible pairs of two letters,
only lower case, one by line, ordered alphabetically.
"""
import string
letter=string.ascii_lowercase
for first in letter:
    for second in letter:
        print(first+second)
