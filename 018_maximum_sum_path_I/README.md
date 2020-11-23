# Problem 018

## [Maximum path sum I](https://projecteuler.net/problem=18)

[<prev](./../017_number_letter_counts/README.md)/[next>](./../019_counting_sundays/README.md) 

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
`Find the maximum total from top to bottom of the triangle below:`
||
|:---:|
|75|
|95 64|
|17 47 82|
|18 35 87 10|
|20 04 82 47 65|
|19 01 23 75 03 34|
|88 02 77 73 07 63 67|
|99 65 04 28 06 16 70 92|
|41 41 26 56 83 40 80 70 33|
|41 48 72 33 47 32 37 16 94 29|
|53 71 44 65 25 43 91 52 97 51 14|
|70 11 33 28 77 73 17 78 39 68 17 57|
|91 71 52 38 17 14 91 43 58 50 27 29 48|
|63 66 04 68 89 53 67 30 73 16 69 87 40 31|
|04 62 98 27 23 09 70 98 73 93 38 53 60 04 23|

**NOTE:** As there are only 16384 routes, it is possible to solve this problem by trying every route. However, 
[Problem 67](https://projecteuler.net/problem=67), 
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method!

### Initial thoughts:
Straight away I think it would be ideal to find a solution to this problem that could also be applied to the related problem 67, but I don't know if that will be possible.\
This problem did turn out to be more difficult than I thought, mathematically. I wasn't sure how to find the solution. The example 4-line triangle is so small that it can be solved by inspection, and the 15-row main triangle is too large for this. \
I tried to solve it manually at first, hoping to find some guidance of how to come to the solution and then at that point starting to figure out how that solution might be translatable to code, or made general. \
I tried starting at the top and picking left or right depending on which was larger. This did not provide the solution. \
Starting at the bottom and working up, picking a dorection based on which was a higher number also did not. \
Finding large numbers near the middle and working 'simultaneously' up and downwards was also fruitless. \

I was clearly in need of assistance, so I got some pointers from a friend who was able to help. \
I was led to consider a possible solution using recursion and considering the effect of what changes if the triangle were to hypothetically have extra rows added. This solution will be illustrated below.

### Pseudocode for first iteration:
```
RECEIVE a triangle of integers

IF the triangle contains only a single integer
THEN return the triangle as an integer
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

RETURN the calculated sum
```

### Comments on first iteration:
This took a while because I'm still relatively inexperienced with using recursion. It did provide the correct solution to this current problem but was not able to calculate the solution to problem 67 as hoped. This is because it is using brute-force, just in a different way.

### Refactoring:
In order to make this more efficient, and hopefully able to solve problem 67, I intend to try to implement some form of memoisation - another technique I am inexperienced in using. 
