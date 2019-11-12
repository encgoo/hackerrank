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