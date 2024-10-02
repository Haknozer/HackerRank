#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    outpouts = ""
    
    for x in range(len(s)):
        if s[x] in alphabet:
            ind = alphabet.index(s[x]) + k
            ind = ind % len(alphabet)
            outpouts += alphabet[ind]
        else:
            if s[x].isupper():
                lowS = s[x].lower()
                ind = alphabet.index(lowS) + k 
                ind = ind % len(alphabet)
                outpouts += alphabet[ind].upper()
            else:
                outpouts += s[x]
                
        
    return outpouts
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
