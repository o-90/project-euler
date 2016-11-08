/**
 * 112)
 * Working from left-to-right if no digit is exceeded by the digit to its left
 * it is called an increasing number; for example, 134468.Similarly if no digit
 * is exceeded by the digit to its right it is called a decreasing number; for
 * example, 66420.  We shall call a positive integer that is neither increasing
 * nor decreasing a "bouncy" number; for example, 155349.  Clearly there cannot
 * be any bouncy numbers below one-hundred, but just over half of the numbers
 * below one-thousand (525) are bouncy. In fact, the least number for which the
 * proportion of bouncy numbers first reaches 50% is 538.  Surprisingly, bouncy
 * numbers become more and more common and by the time we reach 21780 the
 * proportion of bouncy numbers is equal to 90%.
 *
 * Find the least number for which the proportion of bouncy numbers is
 * exactly 99%.
 */

#include <iostream>
#include <string>

using namespace std;


bool is_increasing(int n) {
  string str = to_string(n);

  for (int i=0; i<str.length(); i++) {
    if (i==0)
        continue;

    if (str[i-1] > str[i])
	  return false;
  }
  return true;
}

bool is_decreasing(int n) {
  string str = to_string(n);

  for (int i=0; i<str.length(); i++) {
    if (i==0)
      continue;

    if (str[i-1] < str[i])
      return false;
  }
  return true;
}

bool is_bouncy(int n) {
  if (!(is_increasing(n) || is_decreasing(n)))
    return true;

  return false;
}


int main(int argc, char *argv[]) {

  int count = 0;
  int i = 100;

  while (i <= 2000000) {
    if (is_bouncy(i))
      count++;

    if (i >= 1000000)
      if (i * 0.99 == count)
        break;

    i++;
  }
  cout << "ans = " << i << endl;  // 1587000
  return 0;
}
