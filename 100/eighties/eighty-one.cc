/* ---------------------------------------------------------------------------
 * 81)
 * In the 5 by 5 matrix below, the minimal path sum from the top left to the
 * bottom right, by only moving to the right and down, is indicated in bold
 * red and is equal to 2427.
 *
 *                        131    673   234  103   18
 *                         |
 *                         V
 *                        201 -> 96 -> 342  965   150
 *                                      |
 *                                      V
 *                        630    803   746  422   111
 *                                      |
 *                                      V
 *                        537    699   497  121   956
 *                                      |
 *                                      V
 *                        805    732   524  37 -> 331
 *
 * Find the minimal path sum, in p081_matrix.txt containing a 80 by 80
 * matrix, from the top left to the bottom right by only moving right
 * and down.
 * ---------------------------------------------------------------------------
 */


#include "project_euler_utilities.h"

#include <iostream>
#include <string>


int main(int argc, char** argv) {

  std::vector<std::vector<int>> v;
  std::string path = argv[1];

  load_csv_to_matrix(path, v);

  //  test matrix is loading correctly
  for (int i=0; i<v[0].size(); i++) {
    for (int j=0; j<v[0].size(); j++) {
      std::cout << v[i][j] << " ";
    }
    std::cout << "\n";
  }
  return 0;
}
