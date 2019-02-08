#!/bin/python3

import math
import os
import random
import re
import sys
import time
# Complete the rotLeft function below.

def rotLeft(a, d):
    """
    we join the same array but only taking the first elements and last elements
    marked to rotate
    """
    rotate = d
    rotate_array = a[rotate:] + a[:rotate]

    return rotate_array

if __name__ == '__main__':
    start = time.time()
    """
    20 10
    41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51

    5 4
    1 2 3 4 5
    """
    n = int(20)
    d = int(10)
    a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
    result = rotLeft(a, d)
    print(result)

    end = time.time()
    print("__main__ time-->", end - start)