"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""
import re


def increment_string(strng):
    if strng == "":
        return 1
    if not any(c.isalpha() for c in strng):
        return str(int(strng)+1)
    if any(map(str.isdigit, strng)):
        res = re.findall(r'(\w+?)(\d+)', strng)[0]
        return res[0] + str(int(res[1]) + 1).zfill(len(res[1]))

    return strng + "1"


strng = ""  # foo1
print(increment_string(strng))

strng = "foobar23"  # foobar24
print(increment_string(strng))

strng = "foo0042"  # foo0043
print(increment_string(strng))

strng = "foo9"  # foo10
print(increment_string(strng))

strng = "foo099"  # foo100
print(increment_string(strng))
