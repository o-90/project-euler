# -*- coding: utf-8 -*-


from math import factorial

# 15)
# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

#-----------------------------------------------------------------------------
# Increasing the dimension will create a sequence know as type B Catalan
# Numbers.  1, 2, 6, 20, 70, 252, ... These numbers can be computed using
# max[(i+j)!/(i!j!)] for 0 <= i,j <= n
#-----------------------------------------------------------------------------


def binom(x, y):
    return factorial(x + y) / (factorial(x) * factorial(y))

def func(n):
    tmp = []
    for i in xrange(n+1):
        for j in xrange(n+1):
            tmp.append(binom(i, j))

    return max(tmp)

ans = func(20)

print ans  # 137846528820
