# -*- coding: utf-8 -*-

from itertools import permutations


# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.
#
# What is the largest n-digit pandigital prime that exists?

# We know that the number must end in a 1, 3, 7, or 9.  Also, we know that if
# the sum of a number's digits is 0 mod 3 then the number itself is 0 mod 3 so
# there cannot be a 9(45), 8(36), 6(21) or 5(15)-digit pandigital number that
# is also prime.  So, we only have to search 7-digital.


def sundaram3(max_n):
    """
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    """
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

# primes
dic = {x:1 for x in sundaram3(10000000)}

perms = [''.join(p) for p in permutations([str(x) for x in range(1, 8)], 7)]
perms = [int(x) for x in perms if x[-1] in {'1', '3', '7', '9'}]
perms.sort()

# search biggest ones first
perms.reverse()

for perm in perms:
    if dic.get(perm, None) is not None:
        ans = perm
        break

print ans  # 7652413
