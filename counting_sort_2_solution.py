#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    countingArr = [0 for x in range(100)]
    
    for y in arr:
        countingArr[y] += 1
    
    sortedList = []
    for y in range(len(countingArr)):
        if countingArr[y] != 0:
            for z in range(countingArr[y]):
                sortedList.append(y)
        
    return sortedList
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
