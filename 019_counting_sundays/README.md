# Problem 019

## [Counting Sundays](https://projecteuler.net/problem=19)

[<prev](./../018_maximum_sum_path_I/README.md)/[next>](./../README.md) 

### The example:
`You are given the following information, but you may prefer to do some research for yourself.`

```
- 1 Jan 1900 was a Monday.
- Thirty days has September,
- April, June and November.
- All the rest have thirty-one,
- Saving February alone,
- Which has twenty-eight, rain or shine.
- And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
```

### The challenge:
`How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?`

### Initial thoughts:
Similar to the earlier 
[problem 17](./../017_number_letter_counts.README.md), 
I guess that there probably will be some sort of package available to use with Python that will be capable of providing the solution fairly easily. Also similarl to the earlier problem 17; I will avoid using that route to the solution. Project Euler is a series of challenges with the emphasis on maths, and I'd like to practice applying logic to find my own solution. \
This problem also has some relationship with the popular leap-year kata; which I had heard/talked/thought about before but never actually worked on. I started by 
[completing this kata](https://www.codewars.com/kata/reviews/553a8c52f3cc9482dc000116/groups/553c01f0a21770fd23000002), 
and I may use a copy of this code in my solution here if it is needed. 

My initial approach will be to try to set up some sort of counter that increments in steps of 28, 29, 30 or 31 as appropriate depending on the month; and using some value of the modulo of the total days passed to identify if a day is Sunday or not-Sunday. This way I can count the Sundays.\
Something to note is that the given starting point is January 1900, but no instances of Sunday 1st during 1900 will be included. This will have to be accounted for in whatever solution I develop.

### Pseudocode for first iteration:
```
SET sunday_first_count = 0
SET running total for days_passed = 1*
CREATE a list of days of each month for a Common Year =
  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
CREATE a list of days of each month for a Leap Year =
  [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

PREPARE logic for determining if a year is Leap:
  IF year is divisible by 400
  THEN return True
  ELSE
    IF year is divisible by 100
    THEN return False
    ELSE
      IF year is divisible by 4
      THEN return True
      ELSE return False

FOR each year in range 1900 - 2000 (inc):
  CHECK if year is leap OR common
  FOR each month in the relevant list
    INCREMENT the days_passed by the appropriate number from the list
    IF days_passed is divisible by 7 AND year is greater than 1900
    THEN increment sunday_first_count
    ELSE continue to the next month
```

### Comments on first iteration:
normal text

### Refactoring:
