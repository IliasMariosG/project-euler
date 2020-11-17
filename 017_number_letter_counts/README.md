# Problem 017

## [Number letter counts](https://projecteuler.net/problem=17)

[<prev](./../016_power_digit_sum/README.md)/[next>](./../README.md) 

### The example:
`If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.`

### The challenge:
`If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?`

`NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.`

### Initial thoughts:
I expect there is probably a python library or additional module that could be used to solve this problem very quickly and easily. I have chosen not to pursue this as I would prefer to use it as practice for writing a series of small functions and making sure that they are called correctly; and making sure I am able to construct dictionaries with the correct details.\
I think for this challenge we will be using the `modulo` operator and the `integer division` facility to break numbers down into their respective components which can then be allocated a name (or rather, a number of letters, we do not actually need to gibe every number its name for the answer to be achieved) and the lengths of these names added together within the parameters set in the original challenge.

### Pseudocode for first iteration:
**NB** integer division will be shown using the notation `\`. \
ie. 10\3 = 3 \
cf. 10/3 = 3.3333...
```
CREATE an associative array where:
  KEYS are numbers from 1 to 19 inc. as integers
  VALUES are the length of the word if that number were to be written

CREATE an associative array where:
  KEYS are numbers from 20 to 90 inc., in steps of 10, as integers
  VALUES are the length of the word if that number were to be written

SET the number of letters in 'hundred' = 7
SET the number of letters in 'hundred and' = 10
SET the number of letters in 'one thousand' = 11
SET running total = 0
```
For numbers 19 and under:
```
FOR each integer from 1 to 19 inc.
  ADD the value paired with that number in associative array 1-19 to running total
```
For numbers 20 - 99:
```
FOR each integer from 20 to 99 inc.
  IF the number is divisible by 10
  THEN 
    ADD the value paired with that number in associative array 20-90 to running total
  ELSE
    CALCULATE number\10*10
    ADD the value paired with that number in associative array 20-90 to running total
    AND
    CALCULATE number%10
    ADD the value paired with that number in associative array 1-19 to running total
```
For numbers 100 - 999:
```
FOR each integer from 100 to 999 inc.
  IF the number is divisible by 100
  THEN
    CALCULATE number\100
    ADD the value paired with that number in associative array 1-19 to running total
    AND
    ADD the length of 'hundred' to running total
  ELSE
    CALCULATE number%100
    ADD the value paired with that number in associative array 1-19 to running total
    AND
    ADD the length of 'hundred and' to running total
    AND
    CALCULATE number%100
    USE the function(s) above as appropriate to
      ADD the lengh of the 'tens and units' components to running total
```
Last step:
```
ADD the length of 'one thousand' to running total
RETURN the updated running total as the solution
```

### Comments on first iteration:
At first I tried to break down the sections some more, and include a 'teen' section, It took a few seconds that 13 and 15 are not as straightforward as adding the suffix 'teen' to the unit digit, and a bit longer to realise the same issue with 18. In the end it did not seem necessary to have this 'teen' section so I went with just 1-19 in a single go. \
The code written provided the solution as expected. Also as expected this was a good exercise in making sure functions being called are done so in the correct way and at the correct time. 

### Refactoring:
As I initially suspected, there does appear to be a variety of options of python libraries to use that would have done this calculation  without having to prepare all these functions myself. I will investigate one or more of these in the future.
