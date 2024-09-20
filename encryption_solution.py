#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s = s.split(" ")
    
    counter = 0
    outpouts = ""
    
    lengthString = len(s[0])
    sqrtString = math.sqrt(lengthString)
    column = math.ceil(sqrtString)
    row = math.floor(sqrtString)
    
    if row * column < lengthString:
        row += 1
    
    for x in range(column):
        counter = x
        words = ""
        for y in range(row):
            if counter < lengthString:
                words += s[0][counter]
                counter += column
        
        outpouts += words + " "
    
    return outpouts
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
