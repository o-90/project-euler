# -*- coding: utf-8 -*-

from collections import defaultdict


# 26)
# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
#
#    1/2= 0.5
#    1/3= 0.(3)
#    1/4= 0.25
#    1/5= 0.2
#    1/6= 0.1(6)
#    1/7= 0.(142857)
#    1/8= 0.125
#    1/9= 0.(1)
#    1/10= 0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.  Find the value of d < 1000 for
# which 1/d contains the longest recurring cycle in its decimal fraction part.

def calc_cycle(start, num):
    """
    """
    c = 0
    dic = defaultdict(int)

    while dic.get(start, None) is None:
        dic[start] = c

        new_start = (10 * start) % num
        c += 1
        start = new_start

    return c - dic.get(start)


ans = 2

for x in xrange(2, 1000):
    val = calc_cycle(1, x)
    ans = x if val > ans else ans

print ans  # 983
