# Greedy
Greedy algorithm

## Greedy Florist
This [problem](https://www.hackerrank.com/challenges/greedy-florist/problem) 
is solved by this python [code](greedy_florist.py)

## Max min
For this [problem](https://www.hackerrank.com/challenges/angry-children/problem) we
just need to sort the list first, and then look for the min diff between
k elements.

Python [code](max_min.py)

## Goodland Electricity
This [problem](https://www.hackerrank.com/challenges/pylons/problem) can be 
solved by this python [code](goodland_electricity.py)

## Cloudy Day
 Key points for this [problem](https://www.hackerrank.com/challenges/cloudy-day/problem)
 * Put the start/end point of all the clouds into one list and sort it
 * Combine the x and p lists into a list x_p ```x_p[i] = (x[i], p[i])``` and sort this list
 using ```x[i]```
 * Now hanlde two sorted list according to its location
 
 Python [code](cloudy_day.py)
 
 ## Candies
 This [problem](https://www.hackerrank.com/challenges/candies/problem) can
 be solved by scanning from left to right, and then back from 
 right to left. Start with one candy for the first kid. Implement
 by one if the next kid has a higher score, otherwise reset 
 to 1.
 The right to left scan takes the _max_ of both scan result.
 
 Python [code](candies.py)