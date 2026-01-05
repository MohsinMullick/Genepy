"""

Provide a script printing every possible pairs of two different letters.
Only lower case, one pair per line, ordered alphabetically.
Don't print pairs consisting of twice the same letter, such as 'aa', 'bb', etc...
"""

import string
letters = string.ascii_lowercase
for first in letters:
    for second in letters:
        if first != second:
            print(first + second)
