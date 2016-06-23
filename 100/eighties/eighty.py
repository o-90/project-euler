# -*- coding: utf-8 -*-

# 80)
# It is well known that if the square root of a natural number is not an
# integer, then it is irrational. The decimal expansion of such square
# roots is infinite without any repeating pattern at all.
#
# The square root of two is 1.41421356237309504880..., and the digital
# sum of the first one hundred decimal digits is 475.
#
# For the first one hundred natural numbers, find the total of the digital
# sums of the first one hundred decimal digits for all the irrational
# square roots.


def get_digit_sum(num_digits, n):
    """
    binary-search to get m-number of digits from
    the square root of n
    """
    d = 10 ** num_digits
    n *= d ** 2
    left = 0
    right = n

    while left < right - 1:
        center = (left + right) / 2
        left, right = [[center, right], [left, center]][center ** 2 > n]

    return sum([int(x) for x in str(left)[:-1]])

# test case
assert get_digit_sum(100, 2) == 475

squares = [x ** 2 for x in range(1, 10)]
ans = sum([get_digit_sum(100, x) for x in range(1, 100) if x not in squares])

print ans  # 40886
