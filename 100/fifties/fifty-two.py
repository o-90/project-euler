# -*- coding: utf-8 -*-


# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.


def contains_same(n, k=2):
    """
    """
    m = k * n
    if sorted(str(m)) == sorted(str(n)):
        return True
    return False

# naive way
for i in xrange(1, 1000000):
    if contains_same(i, 2) and contains_same(i, 3) and\
       contains_same(i, 4) and contains_same(i, 5) and\
        contains_same(i, 6):
            ans = i
            break

print ans  # 142857
