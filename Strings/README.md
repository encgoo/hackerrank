# Strings

## String tricks of python
Several useful tricks of python
* Use list(string) to convert a string into list of chars. ''.join(list) converts it back.
* ord(char) and chr(int) to convert between char and int
* Use char_count = [0]*26 to quickly count chars. Useful for anagrams
* for C++, this makes a copy of an array
```
#include <algorithm>
#include <iterator>
using namespace std;
copy(begin(source_array), end(source_array), begin(destination_array));
```
See Common Child for example.

## Examples
### Bear and Steady Gene
This [problem](https://www.hackerrank.com/challenges/bear-and-steady-gene/problem) is solved
using this python [code](bear_and_steady_gene.py).

### Sherlock and Anagrams
This [problem](https://www.hackerrank.com/challenges/sherlock-and-anagrams) can be solved by
this python [code](sherlock_and_anagrams.py)

### Sherlock and valid string
This [problem](https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem) can
by solved by using char_count mentioned before in the tricks. 

Python [code](sherlock_and_valid_string.py)

### Common Child
Some points about this [problem](https://www.hackerrank.com/challenges/common-child/problem)
* A normal approach using DP creates a 2D array of size=s1.size() to store
the information. But when ```s1.size()``` is as big as 5000, this causes memory issue for C++ code.
So somehow the safe guard has memory limitation smaller than 100mb? It shows as
a segmentation error when accessing this array, not when creating this array (quite misleading). The trick is to use only 2 arrays of 5000, instead of
5000 array of 5000.
* The performance validator is unfair for python code here. The exact
same [implementation](common_child.py) in python has timing issue
for Test 9, 11, 12, 13.
* This C++ [code](common_child.cpp) works.

### Highest Value Palindrome
This [problem](https://www.hackerrank.com/challenges/richie-rich/problem) can
be solved by C++ [code](highest_value_palindrome.cpp) 

