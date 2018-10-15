#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for j in range(1,n):
        for i in range(j):
            #print(arr[j],arr[i])
            if(arr[j]<arr[i]):
                t=arr[j]
                arr[j]=arr[i]
                arr[i]=t
        for k in range(n):
            print(arr[k],end=" ")
        print()
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
