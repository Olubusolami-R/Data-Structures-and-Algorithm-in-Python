#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    i=0
    j=0
    sum_num=0
    maximum=float("-inf")
    #ensure to set bundaries with the loops
    while i+2 < len(arr):
        #for row traversal and avoiding overstepping row boundaries
        while j+2 < len(arr):
            #for col traversal and avoiding overstepping col boundaries
            row1=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            row2=arr[i+1][j+1]
            row3=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            sum_num=row1+row2+row3
            #print(i,j)#debugging
            j+=1
            if sum_num>maximum:
                maximum=sum_num
        #print(i)#debugging
        i+=1
        j=0
    return maximum
            
    # Write your code here

def main():

    arr = [
    [0,-4,-6,0,-7,-6],
    [-1,-2,-6,-8,-3,-1],
    [-8 ,-4 ,-2, -8, -8, -6],
    [-3, -1, -2, -5, -7, -4],
    [-3, -5, -3, -6, -6, -6],
    [-3,-6, 0, -8, -6, -7]
    ]
    result = hourglassSum(arr)

    print(str(result) + '\n')

main()
