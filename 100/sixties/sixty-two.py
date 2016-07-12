# -*- coding: utf-8 -*-

from collections import defaultdict


# 62)
# The cube, 41063625 (3453), can be permuted to produce two other cubes:
# 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest
# cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits
# are cube.

# ----------------------------------------------------------------------------
# This isn't terribly efficient
# ----------------------------------------------------------------------------

def is_permutation(n, m):
    """
    check if two numbers are permutations
    """
    return sorted(str(n)) == sorted(str(m))

cubic = lambda x: x ** 3

# generate cubes
cubes = [cubic(x) for x in xrange(346, 10000)]

# only iterate over cubes that have the same sum
cubes_dic = defaultdict(list)
for x in xrange(346, 10000):
    c = cubic(x)
    cubes_dic[sum([int(x) for x in str(c)])].append(c)

# find permutations
g = defaultdict(list)
for i in cubes:
    s_i = sum([int(x) for x in str(i)])
    for j in cubes_dic[s_i]:
        if len(str(i)) < len(str(j)):
            break
        if is_permutation(i, j):
            g[i].append(j)

# find list that has 4 elements in it
for k, val in g.iteritems():
    if len(val) > 3:
        ans = k
        break

print ans  # 127035954683
