import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesOnHouse = 0
    orangesOnHouse = 0
    applesFall = [0]*len(apples)
    orangesFall = [0]*len(oranges)
    for i in range(len(apples)):
        applesFall[i] = a + apples[i]
    for j in range(len(oranges)):
        orangesFall[j] = b + oranges[j]
    for x in applesFall:
        if x >= s and x <= t:
            applesOnHouse +=1
    for y in orangesFall:
        if y >= s and y <= t:
            orangesOnHouse +=1
    print(applesOnHouse)
    print(orangesOnHouse)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
 