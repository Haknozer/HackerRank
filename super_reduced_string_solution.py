#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    length = len(s)
    s = list(s)
    counter = 0
    while True:
        if counter >= length - 1:
            break
            
        if s[counter] == s[counter+1]:
            s.pop(counter)
            s.pop(counter) 
            
            length = len(s)
            counter = 0
        else:
            counter += 1
            
    if length == 0:
        return "Empty String"
    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
