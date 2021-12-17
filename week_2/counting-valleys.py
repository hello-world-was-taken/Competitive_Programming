#QUESTION
#https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps, path):
    # Write your code here
    height = 0
    valley = 0
    for i in path:
        height += 1 if i == 'U' else -1
        valley += 1 if height == 0 and i == 'U' else 0
    return valley
