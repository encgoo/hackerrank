# Recursion
An divide-and-conquer approach. 

Pay attention to when/how to stop the recursion.

## Examples

### Power Sum
This [problem](https://www.hackerrank.com/challenges/the-power-sum/problem)
is a straightforward application of recursion.
Python [code](power_sum.py)

### Crossword Puzzle
The key steps for this [problem](https://www.hackerrank.com/challenges/crossword-puzzle/problem):
* Figure out all the empty/available spaces using recursion, with location
of the first cell, length, and orientation
* Use the information above, we can check the overlapping cell(s) and ensure
the words we fill in don't have conflict.

Python [code](crossword_puzzle.com.py)

### Recursive Digit Sum
This [problem](https://www.hackerrank.com/challenges/recursive-digit-sum/problem)
is quite straightforward.

Python [code](recursive_digit_sum.py)