# -*- coding: utf-8 -*-

import numpy as np
import itertools
from math import sqrt

# 1)
# Find the sum of all the multiples of 3 or 5 below 1000
sum([x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])

# 2)
# Find the sum of the even-valued terms in the Fibonacci sequence
# whose value doesn't exceed 4,000,000

fibs = [1,1]

while fibs[-1] < 4000000:
    fibs.append(fibs[-1]+fibs[-2])

sum([x for x in fibs if x % 2 == 0])

# 3)
# What is the largest prime factor of the number 600851475143 ?

def find_primes(n):
    threshold = int(np.ceil(sqrt(n)))
    for x in xrange(threshold, 0, -1):
        if i % x == 0:
            break

    if x == 1:
        return i
    else:
        return find_primes(x), find_primes(i / x)

max(find_primes(600851475143))

# 4)
# Find the largest palindrome made from the product of two
# 3-digit numbers

# 5)
# What is the smallest positive number that is evenly divisible by
# all the numbers from 1 - 20 ?

# 6)
# Find the difference between the sum of the squares of the first
# 100 natural numners and the square of the sum.

(100*101 / 2)**2 - sum([x**2 for x in xrange(1,101)])

# 7)
# What is the 10001st prime number?


# 8)
# The four adjacent digits in the 1000-digit number that have the
# greatest product are 9 * 9 * 8 * 9 = 5832

'''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''
# Find the thirteen adjacent digits in the 1000-digit number that
# have the greatest product. What is the value of this product?

prods = []
r = r.replace("\n", "")

for i in xrange(1000 - 13 + 1):
    tmp = r[i:i+13]
    p = np.prod([int(char) for char in tmp])
    prods.append(p)

max(prods)

# 9)
# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a**2 + b**2 = c**2
# There exists exactly one Pythagorean triple for which a + b + c = 1000
# Find a*b*c

lst = []
for c in xrange(1,1001):
    for b in xrange(c):
        for a in xrange(b):
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                lst.append((a, b, c))
                break

print np.prod(lst)

# 10)
# Find the sum of the primes less than 2000000

def erat2():
    d = {}
    yield 2

    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = d.pop(q, None)
        if p is None:
            d[q*q] = q
            yield q
        else:
            x = p + q
            while x in d or not (x&1):
                x += p
            d[x] = p

def get_primes_erat(n):
    return list(itertools.takewhile(lambda p: p < n, erat2()))

print sum(get_primes_erat(2000000))
