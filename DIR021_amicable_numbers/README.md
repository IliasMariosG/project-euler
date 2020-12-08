# Problem 021

## [Amicable numbers](https://projecteuler.net/problem=21)

[<prev](./../DIR019_counting_sundays/README.md)/[next>](./../README.md) 

### The example:
`Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).`
`If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.`

`For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.`

### The challenge:
`Evaluate the sum of all the amicable numbers under 10000.`

### Initial thoughts:
In a similar way to the [highly divisible triangular number problem](./../DIR012_highly_divisible_triangular_number/README.md), we will have to identify how many divisors a given number has; although this time we will also need to keep a record of these numbers. \
I will use a similar logic using the square root of the number as the 'midpoint' of the factors and use this to subsequently find all the factors.\
Then after finding the sum of each series of factors; I can check that new number's series of factors to verify if it is amicable.\
It also should be noted that in the example `1` is included as a factor, but `n` itself is not.

### Pseudocode for first iteration:
Get the list of factors
```
SET the list of factors as an empty list
APPEND 1 to the list of factors
RECEIVE an integer
IF the integer is a square number
THEN append the sqare-root to the list of factors
ELSE do nothing

FOR every number < the square root AND > 1
  IF original integer is evenly divisible by this number
  THEN append this number to the list of factors
  ELSE do nothing

FOR every element currently in the list of factors
  NOT including 1
  NOT including the square root (if original integer is square)
  APPEND original integer / list element
```
Check if numbers are 'amicable' and calculate total
```
SET running total = 0
RECEIVE an integer
CALCULATE the sum of its factors
IF the sum of its factors =/= the original integer
THEN calculate the sum of the factors of the new sum
  IF sum of factors of new sum = the sum of factors of the original integer
  THEN the numbers are amicable
    ADD the original integer to the running total
  ELSE continue with the next number
RETURN the running total
```

### Comments on first iteration:
normal text

### Refactoring:
