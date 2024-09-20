import math
import os
import random
import re
import sys


def acmTeam(topic,m):
    outpouts = [0,0]
    
    for x in range(len(topic)):
        for y in range(x+1,len(topic)):
            maxTop = sum(t1 == "1" or t2 == "1" for t1, t2 in zip(topic[x], topic[y]))
            if maxTop > outpouts[0]:
                outpouts[1] = 1
                outpouts[0] = maxTop      
            elif maxTop == outpouts[0]:
                outpouts[1] += 1

    return outpouts
    
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic,m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
