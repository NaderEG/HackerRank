#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    numPositive = 0
    numNegative = 0
    numZero = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            numPositive+=1
        elif arr[i] < 0:
            numNegative+=1
        else:
            numZero+=1

    print(f'{numPositive/len(arr):.6f}')
    print(f'{numNegative/len(arr):.6f}')
    print(f'{numZero/len(arr):.6f}')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
