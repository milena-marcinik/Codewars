# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
# letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
#
# Examples:
#
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"


import re


def spin_words(sentence):
    wordList = re.sub("[^\w]", " ", sentence).split()
    rev_wordList = []
    for word in wordList:
        if len(word) >= 5:
            rev_wordList.append(word[::-1])
        else:
            rev_wordList.append(word)
    return " ".join(rev_wordList)
