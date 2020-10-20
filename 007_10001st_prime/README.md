# Problem 007

## [10001st prime](https://projecteuler.net/problem=7)

[<prev](./../006_sum_square_difference/README.md)/[next>](./../README.md) 

### The example:
`By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.`

### The challenge:
`What is the 10,001st prime number?`

### Initial thoughts:
A prime number has no factors (other than itself and 1) so any number that has any factors is therefore not prime.\
As mentioned previously in 
[Problem 3](./../003_largest_prime_factor.README.md);
a number's square root repersents the median of the list of factors, so if a number has factors, we only need to look on one side of the square root in order to find them. Whether a number is a perfect square or not, the checking will be up to the next integer higher than the square root.\
We do not need to find all, or even more than one. Just identifying one is enough to render a number as 'not prime'.\
Since there is no recognisable pattern to where among the natural numbers primes are located; we will have to check each number in turn to find out if it is prime or not. Then we need to somehow track how many primes we have identified and stop when we get to our target of 10001.

### Pseudocode for first iteration:
```
RECEIVE a number
CALCULATE the square root
ROUND it up to the next integer
RETURN the rounded up square root
```
```
RECEIVE a number 
IF the number is 2
THEN the number is prime
  RETURN True

IF the number is divisible by 2
THEN the number is not prime
  RETURN False

FOR every integer from 2 to the rounded-up-sqare-root
  IF number is divisibile by the current integer
  THEN the number is not prime
    RETURN False
  ELSE continue
```
```
RECEIVE a target number for nth prime
PREPARE an empty list
UNTIL the list contains target number of elements
  FOR all integers starting from 2 and incrementing
    IF integer is prime
    THEN append integer to the list
    ELSE continue with the next integer
RETURN the final element from the list
```

### Comments on first iteration:
I prepared a version of the above pseudocode in Python. This provided the answer as expected. \
There isn't really much more to add; I can't see any other way to identify a given number of prime numbers without looking up the answer somewhere. 

### Refactoring:
The only real idea I have is to avoid using the list, which would save on memory usage and reallocating as the list size grew. Trying to implement some sort of counter that incremented each time a prime number is discovered and then when the target is reached the nth number is returned could be a tactic. This will be something to try in the future.
