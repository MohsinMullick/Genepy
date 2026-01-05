"""
longest word
"""
def longest_word(text):
    words = text.split()
    return max(words, key=len)
print(longest_word("We want a SHRUBBERY"))
print(longest_word("Shrubberies are great"))

