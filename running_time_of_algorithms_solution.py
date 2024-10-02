#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    counter = 0
    
    for x in range(1,len(arr)):
        for y in range(x):
            if arr[x] >= arr[x-1]:
                break
            if arr[y] >= arr[x]:
                arr.insert(y,arr[x])
                if arr[y] == arr[y+1]:
                    counter += x - (y + 1)
                else:
                    counter += x - y
                arr.pop(x+1)
                break
    return counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
