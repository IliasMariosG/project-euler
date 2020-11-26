# Problem 006

## [Sum square difference](https://projecteuler.net/problem=6)

[<prev](./../DIR005_smallest_multiple/README.md)/[next>](./../DIR007_10001st_prime/README.md) 

### The example:

`The sum of the squares of the first ten natural numbers is:`
```
1^2 + 2^2 + ... + 10^2 = 385
```
`The square of the sum of the first ten natural numbers is:`
```
(1 + 2 + ... + 10)^2 = 55^2 = 3025
```
`Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is:`
```
3025 - 3285 = 2640
```
### The challenge:
`Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.`

### Initial thoughts:
At first I tried to discover if there is a relationship between `x` and `sum square difference for 1 to x` and there does appear to be a relationship, which I think is based on `x^4` but I wasn't able to solve any more than that. \
In the absence of discovering a relationship, I decided to iterate through all the numbers and calculate the solution.

### Pseudocode for first iteration:
```
SET range of numbers from 1 - x
SET running total to 0
FOR each number in range
  CALCULATE number ^ 2 
  ADD number ^ 2 to running total
RETURN sum of squares
```
```
SET range of numbers from 1 - x
SET running total to 0
FOR each number in range
  ADD number to running total
CALCULATE total ^ 2
RETURN square of sum
```
```
CALCULATE square of sum - sum of squares
RETURN result
```
### Comments on first iteration:
I prepared a version of the above pseudocode in Python. This provided the result as expected. \
I think there must be a better way to do this calculation. One option is to see if I can find a way to solve the `x^4` relationship mentioned earlier. Another option (inspired by the Project Euler discussion thread) is to see if there is an easier way to solve for the relationship within each 'half' of this problem.

### Refactoring:
Not yet.
