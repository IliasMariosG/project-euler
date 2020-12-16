# Problem 023

## [Non-abundant sums](https://projecteuler.net/problem=23)

[<prev](./../DIR022_names_scores/README.md)/[next>](./../README.md) 

### The example:
`A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.`

`A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.`

`As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.`

### The challenge:
`Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.`

### Initial thoughts:
My initial thought are that I don't think I understand exactly what is needed here. I'll try to work through it systematically and break it down. I've read through the above paragraph a few times and not been able to make sense of it yet.
1. I will need a way to classify numbers as perfect, abundant or deficient - or in this particular case; abundant or 'not abundant'.
1. Get a list of all abundant numbers below some limit; 28,123 seems like a good limit to use; although it might be higher than necessary since we are interested in numbers that are the sum of two abundant numbers, probably 28,111 or even lower would suffice as a limit. I may investigate this later but to begin with I will use 28,123.
1. Check through each integer up to 28,123 and cross reference against the list of all abundant numbers; seeing if the integer can be expressed as the sum of two number in the list.
1. Find all numbers which can be expressed as the sum of two from the list and get the sum of them.

Breaking it down like this has made it seem more straightforward than I initially feared. I think I was thrown off by "this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit" from the example text.\
In order to start; I will use the function already prepared in 
[challenge 21](./../DIR021_amicable_numbers/README.md) 
to give me the list of factors of a number.


### Pseudocode for first iteration:
To classify numbers as abundant or not:
```
USE existing function to get a list of factors of a given number
CALCULATE the sum of these factors
IF the sum is greater than the original number
THEN return True
ELSE return False
```


### Comments on first iteration:
normal text

### Refactoring:
