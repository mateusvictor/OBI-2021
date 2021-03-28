#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    # Write your code here
    print('PARENT', parent)
    print('SIZE', files_size)
    print('\n')
    n = len(parent)
    total = [0 for i in range(n)]
    for i in range(n):
        cur = i
        print('CUR', cur)
        while cur!= -1:
            total[cur] += files_size[i]
            print(f'TOTAL[CUR] = {total[cur]}')
            cur = parent[cur]
            print(f'CUR = {cur}')
        print()

    print("\n\nTOTAL", total)
    val = abs(total[0]-(2*total[1]))
    print('VAL', val)
    for i in range(2, n):
        temp = abs(total[0]-2*total[i])
        if val > temp:
            val = temp
    return val
    
    
if __name__ == '__main__':
    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)
    print(result)
