/* ---------------------------------------------------------------------------
 *  This is free and unencumbered software released into the public domain.
 *
 *  Anyone is free to copy, modify, publish, use, compile, sell, or
 *  distribute this software, either in source code form or as a compiled
 *  binary, for any purpose, commercial or non-commercial, and by any
 *  means.
 *
 *  In jurisdictions that recognize copyright laws, the author or authors
 *  of this software dedicate any and all copyright interest in the
 *  software to the public domain. We make this dedication for the benefit
 *  of the public at large and to the detriment of our heirs and
 *  successors. We intend this dedication to be an overt act of
 *  relinquishment in perpetuity of all present and future rights to this
 *  software under copyright law.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 *  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 *  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 *  IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 *  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 *  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 *  OTHER DEALINGS IN THE SOFTWARE.
 *
 *  For more information, please refer to <http://unlicense.org/>
 * ---------------------------------------------------------------------------
 * -- AUTHOR:     John Martinez <john.r.martinez14@gmail.com>
 * -- DATE:       2017-01-09 14:23:23
 * -- DESCRIPTION:
 * ---------------------------------------------------------------------------
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>


// http://stackoverflow.com/questions/236129
void split(const std::string &s, char delimiter, std::vector<std::string> &elements) {
  std::stringstream std_str;
  std_str.str(s);
  std::string item;
  while (std::getline(std_str, item, delimiter)) {
    elements.push_back(item);
  }
}


int main() {
  std::string line;
  std::ifstream my_file ("/home/nmjrm31/project-euler/data/p081_matrix.txt");

  std::vector<std::vector<std::string>> v;

  if (my_file.is_open()) {
    while (std::getline(my_file, line)) {
      std::vector<std::string> row;
      split(line, ',', row);
      v.push_back(row);
    }
    my_file.close();
  }
  else {
    std::cout << "unable to open file." << std::endl;
  }
  
  // TEST
  std::vector<std::string> first_line = v.front();
  std::vector<std::string> last_line = v.back();
  
  std::cout << "first line: " << std::endl;
  for (int i=0; i<v[0].size(); i++) {
    std::cout << first_line[i] << ' ';
  }
  std::cout << "\n";
  
  std::cout << "last line: " << std::endl;
  for (int i=0; i<v[79].size(); i++) {
    std::cout << last_line[i] << ' ';
  }
  std::cout << "\n";
  
  return 0;
}
