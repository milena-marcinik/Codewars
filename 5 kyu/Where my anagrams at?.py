"""
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array
with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""


def anagrams(word, words):
    anagram = []
    letters = set(word)
    for term in words:
        if all(x in term for x in letters) and len(letters) == len(set(term)) and len(word) == len(term):
            anagram.append(term)

    return anagram

word = "abba"
words = ['aabb', 'abcd', 'bbaa', 'dada']
print(anagrams(word, words))

word = "racer"
words = ['crazer', 'carer', 'racar', 'caers', 'racer']
print(anagrams(word, words))
