# -*- coding: utf-8 -*-

from __future__ import division


# 42)
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
# so the first ten triangle numbers are:
#
#    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the
# word value is a triangle number then we shall call the word a triangle word.
# Using words.txt containing nearly two-thousand common English words, how
# many are triangle words?

# cache alphabet
alphabet = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9,
    'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17,
    'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25,
    'z':26
}

# import file
f = open("../../data/words.txt", 'r')
text = f.readlines()[0].strip().split(',')
text = [x.replace('"', '').lower() for x in text]

# upper bound on triangle number calculation
upper_bound = max([len(x) for x in text])
upper_bound *= 26

# cache triangle numbers
triangle_nums = {}
s = 0
x = 0

while s < upper_bound:
    s = int((x * (x + 1)) / 2)
    triangle_nums[s] = 1
    x += 1

ans = 0

for words in text:
    word_sum = sum([alphabet[x] for x in words])
    in_tri = triangle_nums.get(word_sum, None)
    if in_tri == 1:
        ans += 1

print ans  # 162
