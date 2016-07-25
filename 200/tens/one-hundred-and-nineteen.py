# -*- coding: utf-8 -*-

from math import log, floor


# The number 512 is interesting because it is equal to the sum of its digits
# raised to some power: 5 + 1 + 2 = 8, and 83 = 512. Another example of a
# number with this property is 614656 = 284.  We shall define an to be the
# nth term of this sequence and insist that a number must contain at least
# two digits to have a sum.  You are given that a2 = 512 and a10 = 614656.
#
# Find a30.

# ----------------------------------------------------------------------------
# NOTE:  Rather than calculating every number and then seeing if its
# log(self) / log(digit-sum(self)) forms an integer, can simply check
# exponents until we find ones that have a digit sum equal to its base.
# ----------------------------------------------------------------------------


def sum_digits(n):
    """
    sum the digits of a number n
    """
    n = str(n) if not isinstance(n, str) else n
    return sum([int(x) for x in n])

# assert sum_digits(23) == 5

ans = set()
base = 2

while base < 150:
    base += 1
    exponent = 1
    while base ** exponent < 10**20:
        exponent += 1
        n = base ** exponent
        if sum_digits(n) == base:
            ans.add(n)

print sorted(ans)[29]  # 248155780267521
