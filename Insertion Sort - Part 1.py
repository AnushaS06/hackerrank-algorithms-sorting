#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
        a=arr[n-1]
        flag=0
        for j in range(n-1,0,-1):
            #print(arr[j])
            if(arr[j-1]>a):
                arr[j]=arr[j-1]
            else:
                arr[j]=a
                flag=1    
            for i in range(n):
                print(arr[i],end=" ")
                if(i==n-1):
                    print()
            if(flag==1):
                return;
        if(flag==0):
            arr[0]=a
        for i in range(n):
                print(arr[i],end=" ")
                if(i==n-1):
                    print()
            
            
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
