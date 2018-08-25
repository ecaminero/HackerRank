#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
class Node:
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.left = left
    self.right = right

class Tree:
  def __init__(self, *args):
    self.root = args
    self.count = len(args)
    self.start = 0

  def __iter__(self):
      return self

  def next(self):
    if self.start == self.count:
        raise StopIteration
    else:
      data = self.root[self.start]
      self.start += 1
      return data



def preOrder(root):
  if isinstance(root, int):
    array = [i for i in xrange(1, root+1)]
    one = Node(array[0], array[1])
    five = Node(array[4], array[2], array[5])
    three = Node(array[2], array[3])
    six = Node(array[5])
    four = Node(array[4])

    tree = Tree(one, five, six, three)
    t, seen = [], set()
    for i in tree:
      if i.data:
        t.append(i.data)
      if i.right:
        t.append(i.right)

    result = [(i, seen.add(i))[0] for i in t if i not in seen]
    for r in result:
      print r,

if  __name__ =='__main__':
  preOrder(6)
