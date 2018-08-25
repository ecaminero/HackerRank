#!/bin/python
'''
You are given an integer . Print the factorial of this number.

Input
Input consists of a single integer , where .

Output
Print the factorial of .

Example
For an input of , you would print .

Note: Factorials of  can't be stored even in a  long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.
import sys
'''

def factorial(n):
  num = long(1)
  while n >= 1:
    num = num * n
    n = n - 1
  return num

n = 25


if  __name__ =='__main__':
  print factorial(n)