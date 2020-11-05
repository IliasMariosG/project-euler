# Problem 004

## [Largest palindrome product](https://projecteuler.net/problem=4)

[<prev](./../003_largest_prime_factor/README.md)/[next>](./../005_smallest_multiple/README.md) 

### The example:
`A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.`

### The challenge:
`Find the largest palindrome made from the product of two 3-digit numbers.`

### Initial thoughts:
We will be working with numbers between 100 and 999 (inclusive).\
There is no mathematical relationship between a number and whether it will be palindromic, the only way to tell is to look at it.\
It seems likely, but can't be assumed, that the solution will be the product of two numbers that are high within our range.

There doesn't appear to be a lot to work with here, so my approach will simply be to multiply together numbers sequentially, amd check if the product is a palindrome.\
Collect all the palindromes together and see which one is the largest.

### Pseudocode for first iteration:
```
RECIEVE a number
REVERSE the digits of the received number
IF the original number matches the reversed number
THEN the number is a palindrome
  RETURN True
ELSE the number is not a palindrome
  RETURN false
```
```
SET list of palindromes as an empty list
FOR each number between 999 and 100
  FOR each number between CURRENT NUMBER and 100
    MULTIPLY the two numbers together
    IF the product is a palindrome
    THEN append the product to the list of palindromes
    ELSE do nothing
RETURN the largets entry in the list of palindromes
```

### Comments on first iteration:
I prepared a version of the above peudocode in Python. This provided the answer as expected.\
As described above; there does not appear to be any relationship between one palindromic number and the next, so optimising the search is not likely to be easy. The only one idea so far that I think is worth exploring takes into account the fact that my assumption was correct. The solution does in fact come from two realitively high numbers. Perhaps it is worth 'staggering' the iteration in some way? \
This idea for increasing the efficiency is only valuable if the solution is always relatively high in a generalised version of the problem. \
For the time being this change to the code has not been implemented but remains as a future experiment. 

### Refactoring:
As per the comments above; there is one possible avenue to explore but this will be done in the future.
