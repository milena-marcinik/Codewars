"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
    words = s.split()
    num_of_letters = []
    for word in words:
        num_of_letters.append(len(word))
    return min(num_of_letters)
