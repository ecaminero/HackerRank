#!/bin/python3

import math
import os
import random
import re
import sys


def number_step(number):
  step = 0
  bit = "{:04b}".format(number)
  while bit != '0000':
    step += 1
    number = number >> 1
    bit = "{:04b}".format(number)

  return step

tests = [4, 8, 13, 22, 100]
for number in tests:
  result = number_step(number)
  print(result)
