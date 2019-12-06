# Search
Not sure why search is in a separated category for hackerrank.
Useful tricks:
* Add index to list items, and then sort, using item value. This trick can
be used to figure out how many swaps/insertions needed for sorting a given
list.

# Tricks
## Meet in the middle
An interesting trick that can be explained by a very simple problem.

_Given 4 lists (same length) of integers, pick one from each list, and count how many 
quadruples sum up to 0._

A brute force approach is very straightforward. Use 4 for-loops to get
all the possible combination. This is an O(N<sup>4</sup>) approach.

To improve the performance (with high usage of memory), go though
two for-loops first, and cache the results. Then go though the other 
two for-loops when checking against the cached results.

Python [example](meet_in_the_middle.py)

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

C++ [code](short_palindrome.cpp)

## 8 Cut the Tree
Just use DFS to traverse the tree. Assume node 0 as the root.

Note for python code, since the DFS could be pretty deep when n is big, use
```sys.setrecursionlimit(1000000)```.

Python [code](cut_the_tree.py)

## 9 Beautiful Quadruples
This [problem](https://www.hackerrank.com/challenges/xor-quadruples/problem)
is solved by using "meet in the middle technique". So handle
a and b first. Then merge the result when handling c and d.

Python [code](beautiful_quadruples.py)

## 10 KnightL on a Chessboard
This [problem](https://www.hackerrank.com/challenges/knightl-on-chessboard/problem) can 
be solved by using Dijkstra algorithm. Use a deque and a visited matrix, append all the possible 
next steps into the deque.

Python [code](knightl_on_a_chessboard.py)

## 11 Red Knight's Shortest Path
This [problem](https://www.hackerrank.com/challenges/red-knights-shortest-path/problem) is very
similar to the one above. Again we are going to use Dijkstra algorithm to solve it.

The only different here is that we need to print out the path. So we need to 
store the steps along the path. 

We use a tree structure to store the path. At each cell, there are at most 6 possible
next moves, each of them is a child node of the current node.

We stop when we find the end cell, and we have the end node. We need to trace back to 
the root node. So a parent does not need to know its children. Each child needs to 
remember its parent. 

Python [code](red_knights_shortest_path.py)
