# -*- coding: utf-8 -*-

# 97)
# The first known prime found to exceed one million digits was discovered in
# 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly
# 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1,
# have been found which contain more digits.
#
# However, in 2004 there was found a massive non-Mersenne prime which contains
# 2,357,207 digits: 28433×27830457+1.
#
# Find the last ten digits of this prime number.

i = 0
x = 1
modulus = int(1e10)

while i < 7830457:
  x = 2 * x % modulus
  i += 1

ans = (28433 * x + 1) % modulus
print ans # 8739992577
