#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[8] == "A" and s[:2] == "12":
        return str(int(s[:2])-12)+"0"+s[2:8]
    elif s[8] == "A":
        return s[:8]
    elif s[8] == "P" and s[:2] == "12":
        return str(int(s[:2]))+s[2:8]
    else:
        return str(int(s[:2])+12)+s[2:8]

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
