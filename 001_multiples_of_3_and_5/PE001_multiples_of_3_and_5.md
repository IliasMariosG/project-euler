# Problem 001

## [Multiples of 3 and 5](https://projecteuler.net/problem=1)

### The example:
`If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.`

### The challenge:
`Find the sum of all the multiples of 3 or 5 below 1000.`

### Initial thoughts
This is fairly similar to the popular FizzBuzz kata that I have done before. The main difference is that here we have to provide a total of all the 3s and 5s rather than a list so some sort of function to add together the numbers will be required.\
The typical thing of using a multi-stage IF statement could be used, with care to place the logic in the correct order - dealing with the multiples of 15 first to avoid any accidental mis-identification of these numbers as simply multiples of 3 OR 5 rather than multiples of 3 AND 5.\
Then some sort of running total that is added to each time and returned at the end will be required.

### Pseudocode for first iteration
```
SET running total = 0
FOR each integer less than 1000
  IF the integer is a multiple of 15
  THEN do nothing
  ELSE
    IF the integer is a multiple of 5
    THEN add this integer to running total
    ELSE
      IF the integer is a multiple of 3
      THEN add this integer to running total
      ELSE do nothing
RETURN running total
```

### Coments on first iteration
I prepared a version of the above pseudocode in Python, and this provided the answer as expected. \
Although it works, this solution seems inelegant, and not very easy to manipulate if at any point we wanted to get the total of a different set of numbers, say 3 and 7 (implying then that we ommit multiples of 21)

### Refactoring
The first stage of refactoring is to condense the complicated IF statement outlined above into a simple formula that will provide the total of all multiples of a given number, up to another given limit. 
This can then be called three times, once for each of our two integers (ie 3 and 5) and once for the product of them (ie 15) then a simple piece of arithmetic to add and subtract these numbers as required. \
This also provides the same outcome. This is the form that the code is currently in.
