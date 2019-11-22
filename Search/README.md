# Search
Not sure why search is in a separated category for hackerrank.
Useful tricks:
* Add index to list items, and then sort, using item value. This trick can
be used to figure out how many swaps/insertions needed for sorting a given
list.

# Examples

## 1. Hackerland radio transmitters

python [code](hackerland_radio_transmitters.py)

## 2. Minimum Loss
This [problem](https://www.hackerrank.com/challenges/minimum-loss/problem) can be 
solved by sorting first and then searching.
Python [code](minimum_loss.py).

## 3. Connected Cells in a Grid
This [problem](https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem) can
be solved by recursion, keeping track of visited cells.
Python [code](connected_cell_in_a_grid.py)

## 4. Count Luck
This [problem](https://www.hackerrank.com/challenges/count-luck/problem) is similar
to Connected Cells in a Grid. Use recursive approach and keep check of visited.
Python [code](count_luck.py) 

## 5. Gridland Metro
Two possible approaches for this [problem](https://www.hackerrank.com/challenges/gridland-metro/problem)

* brute-force approach. Create a grid of m*n to track overlapping. 
This approach only works for the first 3 Test Cases. It has runtime error
for all the rest because m*n is too big.
* Use the trick mentioned at the beginning of this post, and then track
overlap.

Python [code](gridland_metro.py)

## 6 Pairs
For this [problem](https://www.hackerrank.com/challenges/pairs/problem) the
brute force approach will be O(N<sup>2</sup>).

To optimize the solution, we can sort the list/vector first, then for
each element ```v``` in the list/vector, we just need to search up 
to ```v + k```. Then it is more like O(N*k).

C++ [code](pairs.cpp)

## 7 Short Palindrome
For this [problem](https://www.hackerrank.com/challenges/short-palindrome/problem) 
there are errors in the given framework for C++ code.
The function to be completed was declared as:
```int shortPalindrome(string s)```
However, the answer is supposed to be modulo (10<sup>9</sup> + 7). So the answer 
can be potentially as big as ```(10<sup>9</sup> + 7) - 1```, which is too big to
be stored in an ```int```. Need to change it to ```unsigned long int```.

C++ [code]()