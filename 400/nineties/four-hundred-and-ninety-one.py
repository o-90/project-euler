# -*- coding: utf-8 -*-



# 491)
# We call a positive integer double pandigital if it uses all the digits
# 0 to 9 exactly twice (with no leading zero). For example, 40561817703823564929
# is one such number.
#
# How many double pandigital numbers are divisible by 11?


# ----------------------------------------------------------------------------
# NOTE:  A number is divisible by 11 if the alternating sum of its digits is
# is also divisble by 11.  If we split the 20 digit number into its 10 even
# digits and its 10 odd digits, we can see that the smallest 10 digit sum is
# bounded below by 2 * (0 + 1 + 2 + 3 + 4) = 20 and the largest is bounded
# above by 2 * (5 + 6 + 7 + 8 + 9) = 70.  We also know that the sum of the 20
# digit number must be equal 90.  So we are looking for numbers x, y s.t.
# 20 <= x,y <= 70, (x - y) = 0 mod 11, and (x + y) = 90.
# ----------------------------------------------------------------------------



