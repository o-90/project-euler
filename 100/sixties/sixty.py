# -*- coding: utf-8 -*-

import networkx as nx


# 60)
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
# them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
# 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
# primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to
# produce another prime.

# ----------------------------------------------------------------------------
# NOTE:  Essentially what we are looking for is a complete subgraph between 5
# nodes, or a 5-clique
# ----------------------------------------------------------------------------

def sundaram(max_n):
    numbers = range(3, max_n+1, 2)
    half = (max_n)//2
    initial = 4

    for step in xrange(3, max_n+1, 2):
        for i in xrange(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + filter(None, numbers)


# generate first 100 million primes
prime_dict = {str(x): True for x in sundaram(100000001)}

# test first 10k primes for concatenation
primes = [str(x) for x in sundaram(10001)]
primes = sorted(primes)

# create edgeset
ans = set()
for k, x in enumerate(primes):
    for y in primes[k:]:
        if prime_dict.get(x+y, False) and prime_dict.get(y+x, False):
            ans.add((x,y))
            ans.add((y,x))

# create graph
g = nx.Graph()
g.add_edges_from(ans)

ans = [x for x in nx.find_cliques(g) if len(x) > 4]
ans = sum([int(x) for x in ans[0]])
print ans  # 26033
