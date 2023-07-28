#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    nums = []
    for i in range(1, max(b)+1):
        for j in b:
            if j%i != 0:
                break
            nums.append(i)

    nums = list(dict.fromkeys(nums))
    print(nums)
    print(a)
    for i in a:
        for j in nums:
            print(j, i, j%i)
            if j%i != 0:
                print("removing", j)
                nums.remove(j)
    print(nums)
    return len(nums)

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()