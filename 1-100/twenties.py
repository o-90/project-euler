#-*- coding: utf-8 -*-



# 20)
#n! means n * (n-1) * ... * 3 * 2 * 1
#
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
#Find the sum of the digits in the number 100!

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

ans = sum([int(x) for x in str(factorial(100))])

# 21)
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n
#which divide evenly into n).  If d(a) = b and d(b) = a, where a ≠ b, then a
#and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
#and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
#142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.

def factors(n):
    """
    http://stackoverflow.com/questions/6800193/
    what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    try:
        return list(set(reduce(list.__add__,
            ([i, n//i] for i in range(2, int(n**0.5) + 1)
            if n % i == 0))))
    except TypeError:
        return [0]

d = {n: sum([1] + factors(n)) for n in xrange(2, 10000)}

want = []

for k in d.keys():
    amicable = d[k]
    if d.get(amicable, None) == k and amicable != k:
        want.append(amicable)
        want.append(k)

ans = sum(list(set(want)))

# 22)
#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing
#over five-thousand first names, begin by sorting it into alphabetical order.
#Then working out the alphabetical value for each name, multiply this value by its alphabetical
#position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth
#3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
#So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?


alphabet = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
  }

f = open("p022_names.txt", 'r')
read = csv.reader(f)

names = [line for line in read][0]
names.sort()

sums = []
for e, name in enumerate(names):
    sums.append((e + 1) * sum([alphabet[x] for x in name.lower()]))

ans = sum(sums)
