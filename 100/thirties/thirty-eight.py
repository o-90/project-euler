# -*- coding: utf-8 -*-



# Take the number 192 and multiply it by each of 1, 2, and 3:
#
#     192 × 1 = 192
#     192 × 2 = 384
#     192 × 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We
# will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product
# of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

# ----------------------------------------------------------------------------
# NOTE: We are given that 918273645 is a solution to this problem so it would
# be fair to assume that the answer to this question is larger than that.
# Therefore, the number that we are looking for is a number that starts with
# a 9 and doesn't contain a zero.  We also know the max digits will have to
# be four.  Any greater than that we have by default a 10-digit number.
# ----------------------------------------------------------------------------

def contains_zeros(n):
    """
    check if an number contains a zero.
    """
    n = str(n) if not isinstance(n, str) else n
    if '0' in n:
        return True
    return False

def unique_digits(n):
    """
    check whether a number has repeating digits or not.
    """
    n = str(n) if not isinstance(n, str) else n
    if len(set(n)) == len(n):
        return True
    return False

def shares_digits(n, m):
    """
    check whether numbers n and m share any digits.
    """
    n = str(n) if not isinstance(n, str) else n
    m = str(m) if not isinstance(m, str) else m
    if set(n).intersection(set(m)):
        return True
    return False

vals = [9] + range(90, 100) + range(900, 1000) + range(9000, 10000)
nums_to_check = [x for x in vals if unique_digits(x) and not contains_zeros(x)]

ans = []

for nums in nums_to_check:

    num = ""
    c = 1

    while True:
        new = nums * c

        if not unique_digits(new):
            break

        if shares_digits(num, new) or contains_zeros(new):
            break

        num += str(new)
        c += 1

    if len(num) == 9:
        ans.append(num)

ans = max(ans)
print ans  # 932718654
