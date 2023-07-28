#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    aliceScore = 0
    bobScore = 0

    for i in range(3):
        if a[i] > b[i]:
            aliceScore += 1
        elif b[i] > a[i]:
            bobScore += 1
    return [aliceScore, bobScore]
    

if __name__ == '__main__':
    fptr = sys.stdout

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()