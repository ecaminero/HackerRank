import string
import time

'''
  Implement an algorithm to determine if a string has all unique characters.
  What if you can not use additional data structure.
'''

stringTest = [
  'Hola',
  'Holo',
  string.ascii_lowercase,
  'Est enim esse veniam Lorem deserunt sunt do proident in anim.',
  'Anim veniam duis cillum irure labore id nisi aute ea nulla.',
  'Incididunt ullamco dolor do ea esse quis eu non quis officia.',
  'Anim fugiat aute ut ullamco sit dolore nulla incididunt commodo ut enim',
  'Nulla anim dolor anim incididunt ipsum magna incididunt eu laboris'
]

def stringUnique(string):
    duplicate = False
    for i, item in enumerate(string):
      if item in string[i+1:]:
        duplicate = True
        break

    return duplicate

start_time = time.time()
if  __name__ =='__main__':
  for string in stringTest:
    print(stringUnique(string))

  print("--- %s seconds ---" % (time.time() - start_time))
