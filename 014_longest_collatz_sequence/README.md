# Problem 014

## [Longest Collatz sequence](https://projecteuler.net/problem=14)

[<prev](./../013_large_sum/README.md)/[next>](./../README.md) 

### The example:
`The following iterative sequence is defined for the set of positive integers:`

```
n → n/2 (n is even)
n → 3n + 1 (n is odd)
```

`Using the rule above and starting with 13, we generate the following sequence:`
```
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```
`It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.`

### The challenge:
`Which starting number, under one million, produces the longest chain?`

`NOTE: Once the chain starts the terms are allowed to go above one million.`

### Initial thoughts:
I've not heard of Collatz sequences before, but they seem straightforward from the discription in this challenge. My initial feeling is that there will not be a straightforward relationship between the starting number and the number of steps in the corresponding sequence. The easiest way to approach this will be to check every number and count the steps. I am happy to make the assumption that every number in the given range has a solution that ends with 1; so this will be how I identify the end point for counting the steps. 

### Pseudocode for first iteration:
```
SET longest observed sequence = 0
SET nuber that resulted in longest sequence = 0

FOR every number up to the limit
  SET collatz sequence length = 0
  BEGIN loop
    IF the number is 1
    THEN 
      IF this collatz sequence length > longest observed sequence
      THEN update longest observed sequence = this sequence length
        UPDATE number that resulted in longest sequence = this number
      ELSE do nothing
    ELSE 
      IF number is even
      THEN divide the number by 2
      ELSE multiply the number by 3 and add 1
      INCREMENT collatz sequence length

RETURN number that resulted in longest sequence
```

### Comments on first iteration:
This solution as outlined above did provide the solution but it took a long time, somewhere around the 1:30 mark. This is longer than is ideal, given the suggestions on the main Project Euler page.\
This indicates that there should be a more efficient method of finding the solution. 

### Refactoring:
The idea that I have for refactoring is:\
Initially record the collatz sequence length for each number, then at each step, see if we have visited this number before, then we will immediately be able to tell how many steps it would take to get down to 1 and add this onto our existing number of steps.
