#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    count = 0
    for j in range(1,n):
        for i in range(j):
            #print(arr[i],arr[j])
            if(arr[j]<arr[i]):
                t=arr[j]
                arr[j]=arr[i]
                arr[i]=t
                count += 1
    
    
    return count
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
