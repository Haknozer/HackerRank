#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    reverseS = list(s)
    reverseS.reverse()
    
    sAscii = []
    reverseSAscii = []
    
    for x,y in zip(s,reverseS):
        sAscii.append(ord(x))
        reverseSAscii.append(ord(y))
        
    for z in range(len(sAscii) - 1):
        if abs(sAscii[z] - sAscii[z+1]) != abs(reverseSAscii[z] - reverseSAscii[z+1]):
            return "Not Funny"
            
    return "Funny"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
