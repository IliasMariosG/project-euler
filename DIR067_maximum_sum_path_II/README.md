# Problem 067

## [Maximum path sum II](https://projecteuler.net/problem=67)

[<prev](./../README.md)/[next>](./../README.md)\
[<prev related](./../DIR018_maximum_sum_path_I/README.md)

### The example:
`By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.`
||
|:---:|
|3|
|7 4|
|2 4 6|
|8 5 9 3|

`That is, 3 + 7 + 4 + 9 = 23.`

### The challenge:
`Find the maximum total from top to bottom in 
`[this](https://projecteuler.net/project/resources/p067_triangle.txt)`
triangle, a 15K text file containing a triangle with one-hundred rows`.

**NOTE:** This is a much more difficult version of 
[Problem 18](https://projecteuler.net/problem=18). 
It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it.

### Initial thoughts:
I was able to solve this problem after solving the related 
[problem 18](./../DIR018_maximum_sum_path_I/README.md), 
but not before learning about the idea of memoisation and trying to learn the basics of how to implement it. This was a good learning process; and I was able to achieve the solution to this problem after a short amount of time puzzling over how the memoisation would work.

### Pseudocode for first iteration:
Based on the pseudocode from problem 18 with some updates:
```
RECEIVE a triangle of integers

IF the triangle contains only a single integer
THEN return the triangle as an integer
ELSE
  IF the triangle has been calculated before
  THEN return the result of this calculation from the cache
  ELSE
    SET 
      top = the first integer in the triangle
      left_part = the part that remains after removal of all integers on the right edge
      right_part = the part that remains after removal of all integers on the left edge

SET
  left_part = the result of recursively calling this function on the left_part
  right_part = the result of recursively calling this function on the right_part

IF the left_part AND right_part are both single integers
THEN add the larger between left and right to the top
ELSE do nothing

ADD the triangle being calculated and its sum to the cache
RETURN the calculated sum
```

### Comments on first iteration:
I am surprised at how effective this memoisation turned out to be. The problem went from being so big that it could never be solved in the timescale of a human lifespan, to now taking ~5&nbsp;s to arrive at a solution. 

### Refactoring:
