
#!/bin/python3
"""
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string.
There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints
* 1 <= |s| <= 100
* 1 <= n <= 10^6
* For  25% of the test cases, n <= 10^6.
Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.
"""


import math
import os
import random
import re
import sys
import time

import signal
def signal_handler(signum, frame):
  raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(120)


# Complete the repeatedString function below.

def repeatedString(s, n):
  """
  It counts the number of "a" in a full string, and in the last, potentially partial string,
  and calculates the total amount of "a" based on that.
  "a" count of full string * number of string repeats + "a" count of last string.
  """
    ocurrence = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    return ocurrence


if __name__ == '__main__':
    start = time.time()
    string = ['cfimaakj', ]
    n = [554045874191]

    try:
      result = repeatedString(string[0], n[0])
    except Exception as msg:
      print("Timed out!")
    else:
      print(result)

      # print(result)
    end = time.time()
    print("__main__ time-->", end - start)
