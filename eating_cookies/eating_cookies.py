#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = {}

def eating_cookies(n, cache={}):
  #base cases
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  #check cache for value
  elif n in cache:
    return cache[n]
  # add value to cache
  else:
    value = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    cache[n] = value
    return value


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')