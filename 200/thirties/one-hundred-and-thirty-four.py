# -*- coding: utf-8 -*-


# 134)
# Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that
# 1219 is the smallest number such that the last digits are formed by p1 whilst
# also being divisible by p2.  In fact, with the exception of p1 = 3 and p2 = 5,
# for every pair of consecutive primes, p2 > p1, there exist values of n for
# which the last digits are formed by p1 and n is divisible by p2. Let S be
# the smallest of these values of n.
#
# Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.


# NOTE: If we have prime pair (p_1, p_2) then the number that we are looking
# for is p_2 * x where x is the smallest solution to p_2 * x = p_1 mod 10^n.
# where n is the number of digits in p_1.


def primes(n):
    """
    Returns  a list of primes < n
    """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def find_n(a, b):
    n = len(str(a))
    x = 10**n
    ans = ((b-a) * pow(x % b, b-2, b)) % b
    return ans*x+a

primes_less_than = primes(1000004)[2:]

ans = 0
for k in xrange(len(primes_less_than)):
    try:
        p1, p2 = primes_less_than[k:(2+k)]
        ans += find_n(p1, p2)
    except ValueError:
        break

print ans  # 18613426663617118
