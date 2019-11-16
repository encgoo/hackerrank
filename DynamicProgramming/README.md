# Dynamic Programming
DP is closely related to recursion.

Some problems when solved using recursion, end up with repeated/overlapping
subproblems. DP can improve efficiency for these problems by avoiding the repeated
subproblems.

In general, there are two approaches.

## Approaches
### Memoization
This is a top-down approach, which is not very different from the recursion approach.
The difference here is to cache the results of the repeated subproblems. 

### Tabulation
This is a bottom up approach. Think of the problem from an induction perspective. 
Build the solution from buttom up.

## Examples

### Equal
This [problem](https://www.hackerrank.com/challenges/equal/problem) is solved by
using tabulation approach. 
Python [code](equal.py)

### Fibonacci Modified
This [problem](https://www.hackerrank.com/challenges/fibonacci-modified/problem) can be 
solved by tabulation approach as well.
Python [code](fibonacci_modified.py)

### Sherlock and Cost
This [problem](https://www.hackerrank.com/challenges/sherlock-and-cost/problem) can
be solved by tabulation approach.
Python [code](sherlock_and_cost.py)

### Sam and Substring
Two approaches for this [problem](https://www.hackerrank.com/challenges/sam-and-substrings/problem).
* Brute force approach
Two for loops. One for length of substring from 1 to len(n) + 1. The inside for loop for start
from 0 to  len(n) - l + 1. Inside this loop take a substring:
```n[start:start + 1]```
This approach works, but has performance issue when n is large
* Smarter approach: python [code]()

### Abbreviation
#### Approach 1
Use recursion. There are repeated sub-problems. 
#### Approach 2: 
Use DP. 
Draw a 2D table

| |_|d|a|B|c|d|
|---|---|---|---|---|---|---|
|_|1 |1 | 0|0 |0 |0 |
|A|0 |0 |1 |0|0 |0 |
|B|0 |0 |0 |1 |0 |0 |
|C|0 |0 |0 |0 |1 |1 |

Python [code](abbreviation.py)

### The Indian Job
### Approach 1
Use recursion. Then this is a O(2<sup>N</sup>).
### Approach 2
Use DP tabulation. Create a 2D matrix
```buildoutcfg
max_holding = [[0]*(N+1) for i in range(G + 1)]
```
Here
```max_holding[i][j]``` holds the information about when g = j, the maximum
time can be put into j, when there are ```arr[0], ..., arr[i]```

Example:
```buildoutcfg
4, 7
5, 2, 3, 4
```
| |0|1|2|3|4|5|6|7|
|---|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|0|
|5|0|0|0|0|0|5|5|5|
|2|0|0|2|2|2|5|5|7|
|4|0|0|2|2|4|5|6|7|
|3|0|0|2|3|4|5|6|7|

Python [code](the_indian_job.py)

