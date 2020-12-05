/**
 * 81)
 * In the 5 by 5 matrix below, the minimal path sum from the top left to the
 * bottom right, by only moving to the right and down, is indicated in bold
 * red and is equal to 2427.
 *
 *                        131    673   234    103   18
 *                         |
 *                         V
 *                        201 -> 96 -> 342    965   150
 *                                      |
 *                                      V
 *                        630    803   746    422   111
 *                                      |
 *                                      V
 *                        537    699   497    121   956
 *                                      |
 *                                      V
 *                        805    732   524 -> 37 -> 331
 *
 * Find the minimal path sum, in p081_matrix.txt containing a 80 by 80
 * matrix, from the top left to the bottom right by only moving right
 * and down.
 * =========================================================================*/

#include "project_euler_utilities.h"

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char **argv) {

  std::vector<std::vector<int>> v;
  std::string path = argv[1];

  load_csv_to_matrix(path, v);

  int i, j, M;
  M = v[0].size(); // v is a square matrix

  for (i = 0; i < M; i++) {
    for (j = 0; j < M; j++) {
      if (i == 0 && j == 0) {
        v[i][j] = v[i][j];
      } else if (j == 0 && i > 0) {
        v[i][j] += v[i - 1][j];
      } else if (i == 0 && j > 0) {
        v[i][j] += v[i][j - 1];
      } else {
        v[i][j] += std::min(v[i - 1][j], v[i][j - 1]);
      }
    }
  }
  std::cout << "ans: " << v[M - 1][M - 1] << std::endl;
  //  ans := 427337
  return 0;
}
