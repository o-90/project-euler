# -*- coding: utf-8 -*-


# 94)
#
# It is easily proved that no equilateral triangle exists with integral length
# sides and integral area. However, the almost equilateral triangle 5-5-6 has
# an area of 12 square units.  We shall define an almost equilateral triangle
# to be a triangle for which two sides are equal and the third differs by no
# more than one unit.
#
# Find the sum of the perimeters of all almost equilateral triangles with
# integral side lengths and area and whose perimeters do not exceed one
# billion (1,000,000,000).


def plus_one(n0, n1, n2):
  return 15*(n2 - n1) + n0

def minus_one(n0, n1):
  return 14*n1 - n0 + 4

mo = []

a = 1
b = 17
perimeter = 2*17+16

while perimeter < 1000000000:
  mo.append(perimeter)
  new_b = minus_one(a, b)
  a = b
  b = new_b
  perimeter = 2*b + (b-1)
  
po = [2*5+6]
a = 1
b = 5
c = 65
perimeter = 2*65+66

while perimeter < 1000000000:
  po.append(perimeter)
  new_c = plus_one(a, b, c)
  a = b
  b = c
  c = new_c
  perimeter = 2*c + (c+1)

ans = sum(mo + po)
print ans  # 518408346
