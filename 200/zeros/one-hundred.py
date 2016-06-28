# -*- coding: utf-8 -*-

from math import sqrt


# 100)
# If a box contains twenty-one coloured discs, composed of fifteen blue discs
# and six red discs, and two discs were taken at random, it can be seen that
# the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
#
# The next such arrangement, for which there is exactly 50% chance of taking
# two blue discs at random, is a box containing eighty-five blue discs and
# thirty-five red discs.
#
# By finding the first arrangement to contain over 1012 = 1,000,000,000,000
# discs in total, determine the number of blue discs that the box would
# contain.


# NOTE: We need to find a solution to the equation (B/T)*(B-1)/(T-1) = (1/2)
# This yields 2B^2 - 2B - (T^2-T) = 0
#
# =>
#
# B = 2 +/- (SQRT(4 + 8(T^2-T))) / 4 or, we need to find an instance above
# 1e12 where 4 + 8(x^2 - x) produces a perfect square.  This a diophantine
# equation with a known recurrence relation.
#
# x[n+1] = 3x[n] + 4y[n]
# y[n+1] = 2x[n] + 3y[n]


def calc(x, y, c=1):
    """
    """
    if x > int(1e12):
        t = (x + 1) / 2
        return int((2 + sqrt(4 + 8 * (t ** 2 - t))) / 4)

    else:
        x_new = 3 * x + 4 * y
        y_new = 2 * x + 3 * y
        return calc(x_new, y_new, c+1)

ans = calc(1, 1)
print ans  # 756872327473
