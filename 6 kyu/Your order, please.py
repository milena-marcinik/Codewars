# Your task is to sort a given string. Each word in the string will contain a single number.
# This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.

def order(sentence):
    def find_num(word):
        for character in word:
            if character.isdigit():
                return int(character)

    words = sentence.split()
    ordered_words = sorted(words, key=find_num)
    return " ".join(ordered_words)
