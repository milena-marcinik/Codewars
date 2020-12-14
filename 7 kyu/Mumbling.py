"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(s):
    repeat_all = ""
    for index, letter in enumerate(s):
        repeat = (index + 1) * letter
        repeat_all += repeat.title() + "-"
    return repeat_all[:-1]
