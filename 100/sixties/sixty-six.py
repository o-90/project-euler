# -*- coding: utf-8 -*-

from math import sqrt, floor
from fractions import gcd


# 66)
# Consider quadratic Diophantine equations of the form:
#
#     x^2 – Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#
# It can be assumed that there are no solutions in positive integers when D
# is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
#     3^2 – 2×2^2 = 1
#     2^2 – 3×1^2 = 1
#     9^2 – 5×4^2 = 1
#     5^2 – 6×2^2 = 1
#     8^2 – 7×3^2 = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
# obtained when D=5.  Find the value of D ≤ 1000 in minimal solutions of x
# for which the largest value of x is obtained.


def find_period(N):
    """
    finds the continued fraction representations
    of irrational square roots
    """
    # initialize
    a_0 = int(floor(sqrt(N)))
    denominator = 1
    a = a_0
    k = 0
    b = 1

    ans = [a_0]

    while True:
        k = (a * denominator) - k
        numerator = sqrt(N) + k
        denominator = (N - k*k) / gcd(N - k*k, b)
        a = int(floor(numerator / denominator))
        b = denominator
        ans.append(a)

        if k == a_0 and b == 1:
            break

    return ans


def find_solutions(l, a=0, b=1):
    if l == []:
        return b / gcd(a, b)
    else:
        x, xs = l[0], l[1:]
        return find_solutions(xs, b, (b*x)+a)


squares = {x*x: True for x in xrange(33)}
test_nums = [x for x in xrange(1001) if not squares.get(x, False)]

ans = {}

for i in test_nums:
    period = find_period(i)

    if len(period) % 2 == 1:
        solution = find_solutions(period[:-1])
    else:
        period = period + period[1:-1]
        solution = find_solutions(period)

    ans[solution] = i

ans = ans[max(ans.keys())]
print ans  # 661
