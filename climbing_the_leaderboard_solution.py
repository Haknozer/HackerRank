#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranked = list(dict.fromkeys(ranked))
    
    playerRanks = []
    playerCount = len(player) - 1
    counter = 0
    
    while playerCount >= 0:
        if counter >= len(ranked) or ranked[counter] <= player[playerCount]:
            playerRanks.append(counter+1)
            playerCount -= 1
        else:
            counter += 1
            
    playerRanks.reverse()
    return playerRanks
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
