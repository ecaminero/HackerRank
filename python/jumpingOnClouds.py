#!/bin/python3

import math
import os
import random
import re
import sys

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def equals(arr):
  bEqual, nTemp = True, arr[0]

  for item in arr:
    if nTemp != item:
      bEqual = False
      break;
  return bEqual

def deletesecure(obj, id):
  try:
    del obj[position-1]
  except :
    pass

  return obj

def jumpingOnClouds(c):
  secure_cloud = {}
  jumping = -1
  for position, cloud in enumerate(c):
    clouds = list(secure_cloud.keys())

    if cloud == 0 and position not in clouds:
      jumping +=1
      temp_ = c[position-2:position]
      slen = len(temp_)

      if slen == 2 and equals(temp_):
        print('temp_', list(secure_cloud.keys()))
        print('position', position-1, position-2)
        secure_cloud = deletesecure(secure_cloud, position-1)
        secure_cloud = deletesecure(secure_cloud, position-2)
        jumping -= 1

      print('temp_2', list(secure_cloud.keys()))
      secure_cloud[position] = cloud
  print(list(secure_cloud.keys()))

  return jumping

if __name__ == '__main__':
    n = int(10)
    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    result = jumpingOnClouds(c)
    print(result)
