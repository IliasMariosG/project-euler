# Problem 016

## [Power digit sum](https://projecteuler.net/problem=16)

[<prev](./../015_lattice_paths/README.md)/[next>](./../README.md) 

### The example:
`2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.`

### The challenge:
`What is the sum of the digits of the number 2^1000?`

### Initial thoughts:
This one seems similar to 
[problem 013](./../013_large_sum/README.md) 
in that is is a fairly straightforward mathematical operation but uses very large numbers. The code that we need to use is going to be fairly straightforward too, only a small amount of built-in methods will be needed.

### Pseudocode for first iteration:
```
CALCULATE the large target number
SPLIT the large number into individual digits
CALCULATE the sum of these digits
RETURN the total
```

### Comments on first iteration:
The code provided the solution as expected. In a similar way to 
[problem 013](./../013_large_sum/README.md), 
I wonder if this may have been more challenging in the past and if I am benefitting from advances in what is available.

### Refactoring:
