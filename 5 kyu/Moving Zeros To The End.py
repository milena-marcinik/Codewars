"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
elements.

move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    array.sort(key=lambda x: (x == 0) and x is not False)
    return array
