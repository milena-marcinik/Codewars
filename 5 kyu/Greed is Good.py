"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw
according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
(contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
In some languages, it is possible to mutate the input to the function. This is something that you should never do. If
you mutate the input, you will not be able to pass all the tests.
"""


def score(dice):
    points = 0

    if dice.count(1) == 5:
        points += 1200
    if dice.count(1) == 4:
        points += 1100
    if dice.count(1) == 3:
        points += 1000
    if dice.count(1) < 3:
        points += 100 * dice.count(1)
    if dice.count(6) == 3:
        points += 600
    if dice.count(5) == 5:
        points += 600
    if dice.count(5) == 4:
        points += 550
    if dice.count(5) == 3:
        points += 500
    if dice.count(5) < 3:
        points += 50 * dice.count(5)
    if dice.count(4) == 3:
        points += 400
    if dice.count(3) == 3:
        points += 300
    if dice.count(2) == 3:
        points += 200

    return points


dice = [2, 4, 4, 5, 4]
print(score(dice))

scores = [2, 3, 4, 6, 2]  # 0
print(score(scores))

scores = [4, 4, 4, 3, 3]  # 400
print(score(scores))

scores = [2, 4, 4, 5, 4]  # 450
print(score(scores))
