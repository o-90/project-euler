# -*- coding: utf-8 -*-


# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.


def is_palindrome(n):
    if isinstance(n, int):
        n = str(n)
    if n == n[::-1]:
        return True
    return False

def int_to_binary(n):
    b = bin(n).split('b')[-1]
    return b

ans = sum([x for x in xrange(1000000) if is_palindrome(x) and is_palindrome(int_to_binary(x))])
print ans #  872187
