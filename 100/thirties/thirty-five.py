# -*- coding: utf-8 -*-


# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100:
#
#     2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?


def sundaram3(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)

def get_rotations(n):
	n = str(n)
	num_len = len(n)

	return set([int(n[-r:] + n[:-r]) for r in xrange(num_len)])


primes = set(sundaram3(1000000))
ans = len([x for x in xrange(1000000) if get_rotations(x).issubset(primes)])

print ans  # 55
