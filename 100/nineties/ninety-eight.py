# -*- coding: utf-8 -*-

from collections import defaultdict
from math import sqrt, floor, ceil

# 98)
# By replacing each of the letters in the word CARE with 1, 2, 9, and 6
# respectively, we form a square number: 1296 = 362. What is remarkable is
# that, by using the same digital substitutions, the anagram, RACE, also forms
# a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram
# word pair and specify further that leading zeroes are not permitted, neither
# may a different letter have the same digital value as another letter.
#
# Using words.txt, a 16K text file containing nearly two-thousand common
# English words, find all the square anagram word pairs (a palindromic word
# is NOT considered to be an anagram of itself).
#
# What is the largest square number formed by any member of such a pair?

# NOTE:  If we contruct a set of available anagrams from the word doc
# provided, we can see that there are anagram pairs that are 9, 8, 6, 5,
# 4, 3, and 2 characters long.  So we will need all perfect squares of
# length 9, 8, 6, 5, 4, 3, and 2 that share the same digits with another
# square.


def is_anagram(a, b):
  """
  check if given two strings are anagrams
  """
  if a != b:
    return sorted(a) == sorted(b)
  return False

def contains_zeros(n):
  """
  check if a square contains zeroes
  """
  n = str(n) if not isinstance(n, str) else n
  return any(x for x in n if x == '0')

def word_permute(n, m):
  """
  given a word has a mapping 0-9 for its characters
  return the permutation of the original words index
  given a second word.
  """
  n = str(n) if not isinstance(n, str) else n
  m = str(m) if not isinstance(m, str) else m
  return ''.join(str(n.index(x)) for x in m)

# import words
f = open("../../data/p098_words.txt", 'r')
text = f.readlines()[0]
word_list = text.replace('"', '').strip().split(',')

dic = defaultdict(list)

for e, word0 in enumerate(word_list):
  for word1 in word_list[e:]:
    if is_anagram(word0, word1):
      dic[len(word0)].append((word0, word1))

word_lens = sorted(dic.keys())
ans = []

for word_len in word_lens[:-2]:
  lower = int(floor(sqrt(10**(word_len-1))))
  upper = int(ceil(sqrt(10**(word_len))))
  squares_to_check = [str(x*x) for x in xrange(lower, upper) if not contains_zeros(x*x)]
  anagrams = dic[word_len]
  for anagram in anagrams:
    perm = word_permute(anagram[0], anagram[1])
    for k, sq_0 in enumerate(squares_to_check):
      for sq_1 in squares_to_check[(k+1):]:
        try:
          if word_permute(sq_0, sq_1) == perm:
            ans.append(max(int(sq_0), int(sq_1)))
            break
        except ValueError:
          continue

ans = max(ans)
print ans  # 18769
