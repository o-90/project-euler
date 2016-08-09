# -*- coding: utf-8 -*-

from primefac import primefac


# 108)
# In the following equation x, y, and n are positive integers.
#
#    (1/x) + (1/y) = (1/n)
#
# For n = 4 there are exactly three distinct solutions:
#
#    (1/5) + (1/20) = (1/4)
#    (1/6) + (1/12) = (1/4)
#    (1/8) + (1/8)  = (1/4)
#
# What is the least value of n for which the number of distinct solutions
# exceeds one-thousand?

# ----------------------------------------------------------------------------
# NOTE:  If we multiply both sides by x and y, we get (x+y)/x*y = 1/n which
# gives nx + ny = x*y or x*y - nx - ny + n*n = n*n; from here we can factor
# the LHS to get (y - n)*(x - n) = n*n.  So, what we are looking for are the
# distinct ways that n^2 can be factored.  Then (#factors + 1)/2 will be the
# number of solutions to the equation.  To find the number n, whose solutions
# are greater than 1000, we need a number n^2 whose factors are > 2000.  We
# know from the fundamental theorem of arithmetic that the number of divisors
# of a number n, d(n), are the product of the exponents of the prime divisors
# of n.  We know that n is a perfect square so we are essnetially looking for
# for the smallest number > 2000 that is a multiple of 5 and 3.
# ----------------------------------------------------------------------------


LIMIT = 8000000
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

tmp = []

for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
            tmp.append((3**x)*(5**y)*(7**z))

smallest = min([u for u in tmp if u > LIMIT])
exponents = [(p-1)/2 for p in primefac(smallest)][::-1]

ans = reduce(lambda x,y: x*y, [x**y for x,y in zip(primes, exponents)])
print ans
