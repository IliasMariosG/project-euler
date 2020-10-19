# Problem 005

## [Smallest multiple](https://projecteuler.net/problem=5)

[<prev](./../004_largest_palindrome_product/README.md)/[next>](./../006_sum_square_difference/README.md) 

### The example:
`2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.`

### The challenge:
`What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?`

### Initial thoughts:
Of course, n! is an example of a number which ould be divisible by al numbers from 1-n, but it is obvious that 10! is much larger than 2520 (from the example) so this is not the way to go.\
I'm not able to identify any technique to solve this problem other than by just checking each number so this will be the method I use.

### Pseudocode for first iteration:
```
SET the range that is to be checked (ie 1-10 or 1-20 etc.)
SET number to check as 1
BEGIN loop
  FOR each integer in range to be checked
    IF number to check % integer from range =/= 0
    THEN this number is not the solution
      INCREMENT number to check
      RESTART loop
    ELSE continue to the next integer
    
    WHEN all integers have been checked
      SOLUTION = number to check
END loop
RETURN number to check
```

### Comments on first iteration:
I prepared a version of the above pseudocode in Python. This provided the answer as expected. \
Although the answer was found, simply iterating through every possibility does not seem satesfactory. It would be good if we were able to discover a more elegant or efficient solution.

### Refactoring:
One small change which could be made to improve the efficiency of the code was the realisation that we do not have to iterate through every number to find our solution. Since the solution is "divisible by all of the numbers [in range]"; then it must be a multiple of the highest number in the range. Therefore we can use the highest number in the range as both the starting point and the increment step when iterating. \
This change was made to the code and the same solution was provided in a much shorter time.\
When investigating how to solve this problem I discovered a more systematic approach, in which I was able to multiply together a sub-set of the integers in the range. The method for eliminating those which are unnecessary requires finding the prime factors of each integer in the range, then seeing which factors are accounted for by other higher integers. This would be complicated to apply in code and does not seem to be more efficient since factorising every integer and then making a series of cross-referrals is a complex process, the result of which is that another complex multiplication would be required.\
For the time being the code has been left as it was after the small change described at the beginning of this section.
