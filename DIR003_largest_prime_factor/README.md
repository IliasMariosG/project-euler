# Problem 003

## [Largest prime factor](https://projecteuler.net/problem=3)

[<prev](./../DIR002_even_fibonacci_numbers/README.md)/[next>](./../DIR004_largest_palindrome_product/README.md) 

### The example:
`The prime factors of 13195 are 5, 7, 13 and 29.`

### The challenge:
`What is the largest prime factor of the number 600851475143 ?`

### Initial thoughts:
It's clear that the `modulo` operation will be useful here; for finding factors, but also checking if numbers are prime, by looking for factors and realising there are none. \
The two stages are:

- find the factors of our number 
- check which are prime and return the largest.

Checking if a number is prime is something I have thought about before through my interest in recreational mathematics. Outside of the special case of square numbers; the factors of numbers come in pairs (a square number's factors are also in pairs other than its sqare root(`sqrt`)) with an equal amount higher than the `sqrt` and lower than the `sqrt`. the factors lower than the `sqrt` are more concentrated and conversely the factors higher than the `sqrt` are spread over a larger range.\
In terms of coding a solution; it seems useful to utilise this phenomenon; as we can greatly reduce how much 'searching' we need to do to check if a number has any factors. Furthermore since the factors come in pairs we can easily deduce the higher ones after we have the lower ones without having to do a systematic search.

So we have a method to find all the factors of a given number. And we can use almost identical logic to deduce if a number is prime or not, so we have what we need to tackle this problem.

### Pseudocode for first iteration:
```
PREPARE empty list for storing the factors
RECEIVE a number
TAKE SQRT of that number
IF SQRT of number is an integer
THEN add the SQRT to the list of factors
ELSE round the SQRT down (specifically down in every case, not natural rounding)
FOR each integer between rounded SQRT and 1 (exclusive)
  IF the original number is exactly divisible by this integer
  THEN add the integer to the list of factors
  ELSE do nothing

FOR each integer in the list of factors
  DIVIDE the original number by this integer
  APPEND the result of this division ot the list of factors*

RETURN the list of factors
```
- *it has been noted that in the event of a number being a perfect square, we will end up with duplicate copies of the SQRT in our list. for a problem such as this, this seems like an acceptable compromise since adding logic to account for this is unlikely to be more efficient than performing a single extra round of calculations. 
```
RECEIVE a list of numbers
SORT the list in decending numerical order
FOR each number in the list
  TAKE the SQRT of the number
  IF the SQRT is an integer
  THEN the number is not prime
    do nothing
  ELSE round the SQRT down (as before)
    FOR each integer between rounded SQRT and 1 (exclusive)
    IF the list-number is divisible by this integer
    THEN the list-number is not prime
      do nothing
    ELSE this list-number is prime 
     RETURN this list-number
```

### Comments on first iteration:
While I'm certain the above logic would work and provide the answer, it does appear to be very complicated and involves iterating oven numbers in ranges multiple times.\
After having a discussion with some colleagues, I realised there was something missing from my mathematical repertoire; I hadn't learned (or have completely forgotten) how to do 
[prime factorisation](https://en.wikipedia.org/wiki/Table_of_prime_factors) 
and that if I could discover a way to implement this style of analysis, it was likely to be more efficient. It would take less code too so in a way it is fortunate that I had these discussions before I tried to program the above pseudocode.

### Refactoring
In an unconventional timeline of events, I refactored my code before I had even written it in the first place. \
What I realised was:\
If we start with any (large-ish) number, and try to divide it by 2 as many times as we can (this could be 0 times or it could be many times) it will eventually result in an odd number.
This new odd number will never be divisible by 2 again; we have by now exhausted that possibility. So we increase our denominator and perform repeated divisions by 3 until we cannot.\
Then we go to the next prime, ie 5, then 7 etc.\
Which implies we need to know the primes. But...\
If a number is not divisible by 2; it is certainly not going to be divisible by 4.\
If a number is not divisible by 3; it is certainly not going to be divisible by 9.\
So even if we try, we only need to try once and it will immediately fail so we will quickly move on to the next integer.\
Once all the divisions yeild the answer of 1, we find the largest number it was divisible by, which will axiomatically be a prime so this will become our answer.

This is the logic that was ultimately used in my Python file.