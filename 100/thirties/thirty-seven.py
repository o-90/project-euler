# -*- coding: utf-8 -*-


# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
# left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.


# ----------------------------------------------------------------------------
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.  Possible
# solutions cannot contain 0, 4, 6, 8 anywhere in the number.  Given those,
# they cannot begin with 1 or 9 and cannot end with 1, 2, 5 or 9
# ----------------------------------------------------------------------------

def begins_with(n, lst=['1', '9']):
    """
    given a list of numbers, will return true if n begins with at least
    one of the numbers in the list, otherwise false.
    """
    n = str(n) if not isinstance(n, str) else n
    return n[0] in lst

def ends_with(n, lst=['1', '2', '5', '9']):
    """
    given a list of numners, will return true if n ends with at least
    one of the numers in the list, otherwise false.
    """
    n = str(n) if not isinstance(n, str) else n
    return n[-1] in lst

def contains(n, lst=['4', '6', '8', '0']):
    """
    numbers cannot contain an even number greater than 2 anywhere
    """
    n = str(n) if not isinstance(n, str) else n
    return any(x for x in n if x in lst)

def is_truncatable(n, lst):
    """
    test truncatability of a number
    """
    n = str(n) if not isinstance(n, str) else n
    num_len = len(n)
    possible = []

    # truncate
    for idx in xrange(1, num_len):
        possible.append(int(n[idx:]))
        possible.append(int(n[:idx]))

    return set(possible) < set(lst)

def sundaram3(max_n):
    """
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
    note: make sure max_n is an odd number.
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

primes = sundaram3(1000001)
prime_dict = {x: True for x in primes}
filtered_primes = [p for p in primes if not begins_with(p)
                     and not ends_with(p) and not contains(p)]
filtered_primes = filtered_primes[2:]  # remove 3 & 7

ans = []
for want in filtered_primes:
    if is_truncatable(want, primes):
        ans.append(want)
        if len(ans) > 10:
            break

ans = sum(ans)
print ans  # 748317
