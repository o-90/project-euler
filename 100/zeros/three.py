# -*- coding: utf-8 -*-

from __future__ import division

# 3)
# What is the largest prime factor of the number 600851475143 ?

def find_max_prime(n):
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i

		i = i + 1

	return int(n)

ans = find_max_prime(600851475143)
print ans  # 6857