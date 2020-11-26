# Problem 020

## [Factorial digit sum](https://projecteuler.net/problem=20)

[<prev](./../DIR019_counting_sundays/README.md)/[next>](./../README.md) 

### The example:
`n! means n × (n − 1) × ... × 3 × 2 × 1`

`For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,`
`and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.`

### The challenge:
`Find the sum of the digits in the number 100!`

### Initial thoughts:
This one seems reminicent of 
[problem 16](./../DIR016_power_digit_sum/README.md) 
in that it will be a fairly straightforward series of mathematical operators albeit using very large numbers. \
Also immediately apparent is that the sum of the digits of `99!` will be the same as that of `100!`, since:\
&nbsp;&nbsp;`100! = 99! * 100`\
and any integer multiplied by 100 has the same digits with an extra `00` at the end. \
In order to create a general solution, I should ignore this fact and actually calculate the answer based on `100!`, but it could be worthwhile to see how much computational time can be saved by using `99!`. This will only remove one step from the process but mathematically it is the largest step.

### Pseudocode for first iteration:
```
RECEIVE an integer
CALCULATE the factorial of that integer
SPLIT the factorial solution into a series of individual digits
ADD together these digits
RETURN the total
```

### Comments on first iteration:
The function described in the pseudocode above did provide the solution as expected. As an experiment I tried the calculation using `99!` and managed to save a whopping 0.000284&#8239;s, so probably not worthwhile compromising the general solution for this saving. 

### Refactoring:
