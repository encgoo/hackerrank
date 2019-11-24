# Implementation

## Tricks

### Accumulator for any pair
If there is a list of integer like
```lst = [1,2,3,4,5,6,7,8]```, pick any two, multiply them. Then sum up all the multiplcation
result.

For a straightforwad approach, this can be implemented by two for loops

``` 
for i in range(len(lst)):
        for j in range(i + 1, len(lst))
```
This approach has a O(N<sup>2</sup>). 

There is a O(N) approach using two accumulators
```
res = 0
acc = 0
for i in lst:
    res += i * acc
    acc += i
```
### C++ sort an array
Use ```#include <algorithm>```, then 
```
int an_array[100] = {....};
std::sort(an_array, an_array + 100);
```
        
## Examples

### Climbing the Leaderboard
[Climbing the leaderboard](https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem) is straightforward.
[code](climbing_the_leaderboard.py)

### 3D Surface Area
This [problem](https://www.hackerrank.com/challenges/3d-surface-area/problem) can be solved 
by this python [code](3d_surface_area.py)

### Forming a Magic Square
This [problem](https://www.hackerrank.com/challenges/magic-square-forming/problem) can be solved
by this C++ [code](magic_square_forming.cpp)

### The Grid Search
This [problem](https://www.hackerrank.com/challenges/the-grid-search/problem) can be solved by 
this C++ [code](the_grid_search.cpp)

### Ema's Supercomputer
This [problem](https://www.hackerrank.com/challenges/two-pluses/problem) can be solved by
this python [code](emas_supercomputer.py)

### Organizing Containers of Balls
The keypoint for this [problem](https://www.hackerrank.com/challenges/organizing-containers-of-balls/copy-from/128756445) 
is that when you swap balls, the number of balls in each container remains the same. 

C++ [code](organizing_containers_of_balls.cpp)