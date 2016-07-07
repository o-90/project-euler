# -*- coding: utf-8 -*-


# 19)
# You are given the following information, but you may prefer to do some
# research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.  How many Sundays fell on the first of the
# month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# accumulation function
def acc(l):
    total = 0
    for x in l:
        total += x
        yield total

# count number of Sunday's in a list
def num_sundays(lst):
    return sum([1 for x in lst if x % 7 == 6])

# days in a month
yr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_yr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# accumulated days in a month
yr = [x for x in list(acc([1] + yr[:-1]))]
leap_yr = [x for x in list(acc([1] + leap_yr[:-1]))]

# prelims
ans = 0
days = 0

for year in xrange(1901, 2001):
    if year % 4 == 0:
        l = [x + days for x in leap_yr]
        days += 366
    else:
        l = [x + days for x in yr]
        days += 365

    ans += num_sundays(l)

print ans  # 171
