#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p=arr[0]
    right = []
    left = []
    equal = []
    for i in range(1,len(arr)):
        if(p<arr[i]):
            right.append(arr[i])
        elif(p>arr[i]):
            left.append(arr[i])
        else:
            equal.append(arr[i])
    a = []
    for i in range(len(left)):
        a.append(left[i])
    a.append(p)
    for i in range(len(right)):
        a.append(right[i])
    return(a)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
