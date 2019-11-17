# Dynamic Programming
DP is closely related to recursion.

Some problems when solved using recursion, end up with repeated/overlapping
subproblems. DP can improve efficiency for these problems by avoiding the repeated
subproblems.

In general, there are two approaches.

## 1. Approaches
### 1.1 Memoization
This is a top-down approach, which is not very different from the recursion approach.
The difference here is to cache the results of the repeated subproblems. 

### 1.2 Tabulation
This is a bottom up approach. Think of the problem from an induction perspective. 
Build the solution from buttom up.

## 2. Examples

### 2.1 Equal
This [problem](https://www.hackerrank.com/challenges/equal/problem) is solved by
using tabulation approach. 
Python [code](equal.py)

### 2.2 Fibonacci Modified
This [problem](https://www.hackerrank.com/challenges/fibonacci-modified/problem) can be 
solved by tabulation approach as well.
Python [code](fibonacci_modified.py)

### 2.3 Sherlock and Cost
This [problem](https://www.hackerrank.com/challenges/sherlock-and-cost/problem) can
be solved by tabulation approach.
Python [code](sherlock_and_cost.py)

### 2.4 Sam and Substring
Two approaches for this [problem](https://www.hackerrank.com/challenges/sam-and-substrings/problem).
* Brute force approach
Two for loops. One for length of substring from 1 to len(n) + 1. The inside for loop for start
from 0 to  len(n) - l + 1. Inside this loop take a substring:
```n[start:start + 1]```
This approach works, but has performance issue when n is large
* Smarter approach: python [code]()

### 2.5 Abbreviation
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

### 2.6 The Indian Job
Two possible approaches for this [problem](https://www.hackerrank.com/challenges/the-indian-job/problem)
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

### 2.7 Coin Change
This [problem](https://www.hackerrank.com/challenges/coin-change/problem) is similar to "The Indian Job" above. 

The keypoint of using DP tabulation is to figure out what information to hold.
Again a 2D matrix
```buildoutcfg
max_ways[[0]*(n + 1) for _ in range(len(c) + 1)]
```
Here```max_ways[i][j]``` holds the information when n = j, the maximum ways of different
changes given only ```c[0],...,c[i - 1]``` coins are given.

Example:
```
4,3
1,2,3
```
Then ```max_ways[2][3]``` means n = 3, and coins are (1,2). So to make 3 using
only two kinds of coins (1,2) we can have 2 ways {1,1,1}, {1, 2}

The whole table is

| |0|1|2|3|4|
|---|---|---|---|---|---|
|1|1|1 |1 |1 |1 |
|2|1|1|2|2|3|
|3|1|1|2|3|4|

Python [code](coin_change.py) 

### 2.8 The Maximum Subarray
We need to compute max of subsequence and subarray for this [problem](https://www.hackerrank.com/challenges/maxsubarray/problem)

First of all, since empty subsequence or empty sybaray is not allowed, we 
are going to handle these two cases separately.
1. If all elements are negative (or say the max is negative), the subsequence and the 
subarray with max sum are the same
```[max]```
2. If there are at least 1 positive element, the sum for subsequence is simple.
Just sum all the positive elements.
To get the max subarray, we need to use [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane.27s_algorithm)

Python [code](the_maximum_subarray.py)

### 2.9 Knapsack 
This [problem](https://www.hackerrank.com/challenges/unbounded-knapsack/problem) is 
very similar to 2.7 Coin Change above. 

Use a 2D table. The horizontal axis is ```k```, for the target sum.
The vertical axis for ```arr[i]```. The first row, means using none from ```arr```
The second row means using only ```arr[0]```. The third row means using```arr[0], and arr[1]```

Example:
```buildoutcfg
3 10
2 3 4
```
| |0|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|---|
| |0|0|0|0|0|0|0|0|0|0|0|
|2|0|0|2|2|4|4|6|6|8|8|10|
|3|0|0|2|3|4|5|6|7|8|_9_|10|
|4|0|0|2|3|4|5|6|7|8|9|10|
Explanation:
To get the value 9 (the _italic_ font one) of the third row of the above table, 10th column, we are going through these steps:
* First, check the one in the above row. If the one there is the same as k, then we
have nothing to do. Just copy it down. This is not the case here. It means without the new
arr[1]=3, using currently available, the best is only 8, not 9 yet. So we want to check
if the newly available 3 can make things better.

* Using the data of the above row, move back 3 (for k = 6). See if add a 3 there can make 
things better. It is a 6 there. So adding a 3 will make it a 9. 9 is better than 8. So we
can keep it. We can move back 3 more to check, until to the end of the above row in general. 

Python [code](knapsack.py)  