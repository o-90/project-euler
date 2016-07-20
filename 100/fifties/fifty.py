# -*- coding: utf-8 -*-

# The prime 41, can be written as the sum of six consecutive primes:
#     41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.  The longest sum of consecutive primes below one-thousand that
# adds to a prime, contains 21 terms, and is equal to 953.  Which prime, below
# one-million, can be written as the sum of the most consecutive primes?


def sundaram(max_n):
    """
    generate number of primes less than a given quantity.
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

def accumu(lis):
    """
    could modify this to be a dictionary and keep a count of the number of
    iterations which would be the sum length
    """
    total = 0
    count = 0
    for x in lis:
        total += x
        count += 1
        yield total, count

# generate a list and dictionary of primes
primes = sundaram(1000001)
prime_dict = {p: True for p in primes}

# initialize containers
i = 0
ans = {}

# this could be better; def a bit hacky
while i < 4:
    for k, v in accumu(primes[i:]):
        if k < 1000000 and prime_dict.get(k, False):
            ans[k] = v

    i += 1

# get max key
ans_key = max(ans.values())

# reverse dict
d = {v:k for k,v in ans.iteritems()}

ans = d[ans_key]
print ans  # 997651
