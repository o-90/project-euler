# -*- coding: utf-8 -*-


# 57)
# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.
#
#     √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# By expanding this for the first four iterations
# we get:
#
#     1 + 1/2 = 3/2 = 1.5
#     1 + 1/(2 + 1/2) = 7/5 = 1.4
#     1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#     1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the
# numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a
# numerator with more digits than denominator?


num_length = lambda n: len(str(n))


ans = 0

for k in xrange(1000):

    # initialize
    numerator = 1
    denominator = 2
    count = 0

    while count < k:
        numerator = 2 * denominator + numerator
        numerator, denominator = denominator, numerator
        count += 1

    if num_length(numerator + denominator) > num_length(denominator):
        #print "{} / {}".format(numerator + denominator, denominator)
        ans += 1

print ans  # 153
