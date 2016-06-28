# -*- coding: utf-8 -*-

from collections import defaultdict


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




def num_ranges(n):
    """
    only get squares that are of length 10 or less.
    """
    if len(str(n)) < 11:
        return True
    else:
        False


def is_anagram(x, y):
    """
    returns T/F whether two strings are anagrams or not
    """
    return sorted(x) == sorted(y)

# import words
f = open("../../data/p098_words.txt", 'r')
text = f.readlines()[0]
word_list = text.replace('"', '').strip().split(',')

# create word graph
word_graph = defaultdict(list)
for e, word_1 in enumerate(word_list):
    for word_2 in word_list[(e+1):]:
        if is_anagram(word_1, word_2):
            word_graph[word_1].append(word_2)


#squares = [n**2 for n in xrange(100000) if num_ranges(n**2)]


#int(''.join([x for x, y in sorted(zip('reduction', '685072341'), key=lambda x: x[1])]))




