# -*- coding: utf-8 -*-


# 28)
# Starting with the number 1 and moving to the right in a clockwise direction
# a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
# formed in the same way?

tmp = []

def calc(lst, c=0):
	"""
	"""
	if c // 8 == 500:
		return 0

	else:
		new_list = [x + c for x in range(2, 10, 2)]
		out_list = [x + y for x, y in zip(lst, new_list)]
		tmp.extend(out_list)

		return calc(out_list, c+8)

calc([1]*4)
ans = 1 + sum(tmp)
print ans  # 669171001