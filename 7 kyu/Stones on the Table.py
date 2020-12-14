"""
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters
R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent
stones have different colours.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9
"""


def solution(stones):
    result_list = list(stones[0])
    for letter in stones[1:]:
        if letter != result_list[-1]:
            result_list.append(letter)
    return len(stones) - len(result_list)
