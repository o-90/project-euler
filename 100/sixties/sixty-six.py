# -*- coding: utf-8 -*-

from math import floor, sqrt
import argparse

# Consider quadratic Diophantine equations of the form:
#
# x^2 – Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#
# It can be assumed that there are no solutions in positive integers when
# D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we
# obtain the following:
#
# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the
# largest x is obtained when D=5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the
# largest value of x is obtained.

'''
https://www.physicsforums.com/threads/how-to-solve-pells-equation.37854/

Assume D is not a perfect square. To find the continued fraction expression
of sqrt(D), we first set a[0] = floor(sqrt(D)).  This is a very crude
approximation to sqrt(D).  At this point we have
sqrt(D) = a[0] + (sqrt(D) + a[0]) = a[0] + 1/1/(sqrt(D) - a[0])
We apply the same procedure to
1/(sqrt(D) - a[0]) = (sqrt(D) + a[0])/(D - a[0] ** 2)
and get
a[1] = (sqrt(D) + a[0]) / (D - a[0] ** 2)
Now we have
sqrt(D) = a[0] + 1/(a[1] + (sqrt(D) + a[0])/(D - a[0]**2)) + a[1])
repeat.
'''
parser = argparse.ArgumentParser()
parser.add_argument("--num", type=int, default=14)
args = parser.parse_args()

c = 0
keep_track = []
D = args.num

sqrt_D = sqrt(D)
a_0 = floor(sqrt(D))
keep_track.append(a_0)


while c < 25:
	sqrt_D = 1. / (sqrt_D - a_0)
	a_0 = floor(sqrt_D)
	keep_track.append(a_0)
	c += 1

print keep_track
