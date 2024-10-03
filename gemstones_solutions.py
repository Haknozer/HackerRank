#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    counter = 0
    arr[0] = list(dict.fromkeys(arr[0]))
    for x in arr[0]:    
        controller = True
        for y in range(1,len(arr)):
            if x not in arr[y]:
                controller = False
                break
        if controller == True:
            print(x)
            counter += 1
            
    # -------------------------------   
    # OR
    # duplicateItems = []
    # for x in arr[0]:    
    #     if x in duplicateItems:
    #         continue
    #     duplicateItems.append(x)
    #     controller = True
    #     for y in range(1,len(arr)):
    #         if x not in arr[y]:
    #             controller = False
    #             break
    #     if controller == True:
    #         print(x)
    #         counter += 1
        
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
