#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    count = 0
    for x in range(n-1,0,-1):
        if count > arr[x-1]:
            arr[x] = count
            break
        if arr[x] < arr[x-1]:
            count = arr[x]
            arr[x]= arr[x-1]
        if arr[x-1] < arr[x]:
            arr[x],arr[x-1] = arr[x-1],arr[x-1]
            
        print(*arr)
    if arr[0] > count:
        arr[0] = count
    print(*arr)
    
        
   
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
