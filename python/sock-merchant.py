#!/bin/python3
"""
link https://www.hackerrank.com/challenges/sock-merchant/problem
"""

import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
  sock_pairs = 0
  tem_sock_pairs = {}

  for sock in ar:
    key = str(sock)
    if key not in tem_sock_pairs:
      tem_sock_pairs[key] = 1
    elif key in tem_sock_pairs:
      tem_sock_pairs[key] += 1
    
    if tem_sock_pairs[key] == 2:
      sock_pairs += 1
      del tem_sock_pairs[key]
     
  return sock_pairs


# Input
# 9
# 10 20 20 10 10 30 50 10 20


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()