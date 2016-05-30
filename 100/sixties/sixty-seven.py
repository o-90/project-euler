# -*- coding: utf-8 -*-

import numpy as np
import csv

# 67)

# By starting at the top of the triangle below and moving to adjacent numbers on
# the row below, the maximum total from top to bottom is 23.
#
# 			3
# 		       7 4
# 		      2 4 6
#  		     8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in big_triangle.txt, a text file
# containing a triangle with one-hundred rows.

f = open("../../data/big_triangle.txt", 'r')
read = csv.reader(f)

arr = np.zeros((100, 100))

# populate array with triangle
for i, line in enumerate(read):
    nums = line[0].split(" ")
    for j, num in enumerate(nums):
        arr[i][j] = int(num)

for i in xrange(1, len(arr)):
    for j in xrange(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif i == j:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += np.maximum(arr[i-1][j], arr[i-1][j-1])

ans = int(np.max(arr[-1]))
print ans  # 7273
