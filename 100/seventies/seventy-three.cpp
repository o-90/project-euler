/**
 * 73)
 * Consider the fraction, n/d, where n and d are positive integers. If n<d and
 * HCF(n,d)=1, it is called a reduced proper fraction.  If we list the set of
 * reduced proper fractions for d ≤ 8 in ascending order of size, we get:
 *     1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
 *     2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
 *
 * It can be seen that there are 3 fractions between 1/3 and 1/2.
 *
 * How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
 * proper fractions for d ≤ 12,000?
 */

#include <iostream>
#include <cmath>


// function to compute the greatest common divisor
// between two numbers
int gcd(int a, int b) {
  int c = a % b;
  while(c != 0) {
    a = b;
    b = c;
    c = a % b;
  }
  return b;
}


int main(int argc, char* argv[]) {

  int count = 0;

  for (int i = 1; i <= 12000; i++) {
    for (int j = ceil(i/3.); j < ceil(i/2.); j++) {
      if (gcd(i, j) == 1)
        count++;
    }
  }

  std::cout << "ans: " << count - 1 << std::endl;
  // 7295372
 
  return 0;
}
