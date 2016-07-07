# -*- coding: utf-8 -*-

import networkx as nx
from collections import defaultdict


# 95)
# The proper divisors of a number are all the divisors excluding the number
# itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
# the sum of these divisors is equal to 28, we call it a perfect number.
#
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of
# the proper divisors of 284 is 220, forming a chain of two numbers. For this
# reason, 220 and 284 are called an amicable pair.
#
# Perhaps less well known are longer chains. For example, starting with 12496,
# we form a chain of five numbers:
#
#    12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
#
# Since this chain returns to its starting point, it is called an amicable chain.
# Find the smallest member of the longest amicable chain with no element exceeding one million.

# NOTE: There is probably a much better way to do this.

def sum_factors(n):
    """
    """
    f = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    f = list(sorted(f))
    return sum(f[:-1])

d = {}
for x in range(1, 10000):
    n = x
    while not (d.has_key(n) or n < 1 or n > 1000000):
        sf = sum_factors(n)
        d[n] = sf
        n = sf

pairs = [(k, v) for k, v in d.iteritems()]
G = nx.DiGraph(pairs)
all_cycles = nx.simple_cycles(G)

ans = []
max_cycle = 0
for cycle in all_cycles:
    cycle_len = len(cycle)
    if cycle_len > max_cycle:
        ans = cycle
        max_cycle = cycle_len

ans = min(ans)
print ans  # 14316
