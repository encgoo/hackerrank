# Recursion
An divide-and-conquer approach. 

Pay attention to when/how to stop the recursion.

## Examples

### 1. Power Sum
This [problem](https://www.hackerrank.com/challenges/the-power-sum/problem)
is a straightforward application of recursion.
Python [code](power_sum.py)

### 2. Crossword Puzzle
The key steps for this [problem](https://www.hackerrank.com/challenges/crossword-puzzle/problem):
* Figure out all the empty/available spaces using recursion, with location
of the first cell, length, and orientation
* Use the information above, we can check the overlapping cell(s) and ensure
the words we fill in don't have conflict.

Python [code](crossword_puzzle.com.py)

### 3. Recursive Digit Sum
This [problem](https://www.hackerrank.com/challenges/recursive-digit-sum/problem)
is quite straightforward.

Python [code](recursive_digit_sum.py)

### 4. Password Cracker
This [problem](https://www.hackerrank.com/challenges/password-cracker/problem) 
can be solved by recursion on moving an index forward. 
Because different paths might re-check the same i, so
use an array ```checked = [False]*len(loginAttempt)``` to store the information

One more point, default python recursion limit is only 5000. Need to 
increase it to pass all the tests.

Python [code](password_cracker.py)

### 5. Stone Division, Revisited
This [problem](https://www.hackerrank.com/challenges/stone-division-2/problem) can be 
solved by straightforward recusion. But there are repeated subproblems.

The DP approach uses straightforward memoization. So this belongs more to the DP section.

Python [code](stone_division_2.py)