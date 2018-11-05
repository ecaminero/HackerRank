#!/bin/python3

import math
import os
import random
import re
import sys

def exist(data, position):
  try:
    data[position]
    return True
  except Exception as e:
    return False

def hasHourglass(column, row, arr):
    done = False
    completeHourglass = False
    start = row
    result = 0;
    temHourglass = []
    validation = 3
    middle = False

    while not done:
      valid = exist(arr[column], row)
      done = not valid
      print(temHourglass)
      if completeHourglass:
        result = sum(temHourglass)

        break;

      if valid and validation >= 0:
          temHourglass.append(arr[column][row])
          row += 1
          validation -= 1

      if(validation <= 0):
          if middle:
            validation = 3
            row = start
          else:
            validation = 1
            row = start+1
          column += 1
          middle = not middle
      if not exist(arr, column):
          break;
      completeHourglass = (len(temHourglass) == 7)

    return result



# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = []

    for column, datalist in enumerate(arr):
        for row, data in enumerate(datalist):
            result = hasHourglass(column, row, arr)
            hourglasses.append(result)
    hourglasses.sort(reverse=True)
    return hourglasses[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()