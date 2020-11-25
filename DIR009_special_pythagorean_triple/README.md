# Problem 009

## [Special Pythagorean triple](https://projecteuler.net/problem=9)

[<prev](./../DIR008_largest_product_in_a_series/README.md)/[next>](./../DIR010_summation_of_primes/README.md) 

### The example:
`A Pythagorean triplet is a set of three natural numbers, a < b < c, for which:`

```
a^2 + b^2 = c^2
```
`For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.`

### The challenge:
`There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.`

### Initial thoughts:
As per the example, `c` must be the largest of the three numbers in the triple. Although right-angled triangles can be isosceles, in this instance we are not looking for one since the problem states that `a < b`; and in any case 
[it is not possible that an isosceles triangle can be a pythagorean triple](https://en.wikipedia.org/wiki/Special_right_triangle#:~:text=%3A305-,Almost%2Disosceles%20Pythagorean%20triples,isosceles%20right%20triangles%20do%20exist.)
.\
Also it is understood that in order for a set of three numbers to form a triangle at all; 
[the largest among them must be **less than** half of the combined total.](https://www.codewars.com/kata/reviews/56654b518dd05b11d1000049/groups/5dda5a4e26312500014bbb12) 
This means that the length of the hypotenuse must be less than 500, so we only need to consider numbers below 499.\
Within the scope of this challenge it doesn't actually matter whether `a` or `b` is larger, the result would be the same. In a more general version of this problem where this 
<b>
  was
</b> 
important, it would be necessary to somehow sort the resulting three integers before presenting the solution.


### Pseudocode for first iteration:
```
RECEIVE three integers
FIND the largest of the three
  ALLOCATE this as `c`
ALLOCATE the others as `a` and `b`

CHECK
IF a^2 + b^2 = c^2
THEN the three numbers are a pythagorean triple
  RETURN true
ELSE the numbers are not a pythagorean triple
  RETURN false
```
```
FOR every value < 499
  ALLOCATE this value as c
  FOR every value less than c
    ALLOCATE this value as a
    SET b = 1000 - c - a
    
    CHECK
    IF a, b, and c are a pythagorean triple
    THEN this is the solution
      RETURN the product a * b * c
    ELSE this is not the solution
      CONTINUE checking more numbers
```

### Comments on first iteration:
The solution was found by using the approach outlined above; using Python. \
I don't think there is much to comment on here; my understanding of this challenge is that this is the way to discover the solution.

### Refactoring:
