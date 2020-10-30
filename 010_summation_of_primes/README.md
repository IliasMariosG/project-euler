# Problem 010

## [Summation of primes](https://projecteuler.net/problem=10)

[<prev](./../009_special_pythagorean_triple/README.md)/[next>](./../README.md) 

### The example:
`The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.`

### The challenge:
`Find the sum of all the primes below two million.`

### Initial thoughts:
Another challenge where we need to check if a number is prime or not; so maybe we can reuse the function written in challenge 7  for this. \
We need to check each number under 2 million. If the number is prime we will add it to a list and at the end we add together all the numbers in the list and this will be the total. 

### Pseudocode for first iteration:
```
CREATE an empty list ready to receive prime numbers
CHECK all numbers less than the limit
  IF the number is prime
  THEN append it to the list
  ELSE do nothing.

CALCULATE the sum of all numbers in the list
RETURN this total
```

### Comments on first iteration:
The above method provided the solution as expected.

### Refactoring:
It seems unneccessary to create the list before calculating the sum. Another approach would be to set up a running total and do each addition in turn as a prime was found. It possibly would not provide the answer more quickly but would require the use of less memory.\
This will be done in the future.
