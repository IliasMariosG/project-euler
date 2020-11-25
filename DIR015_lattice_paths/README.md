# Problem 015

## [Lattice paths](https://projecteuler.net/problem=15)

[<prev](./../DIR014_longest_collatz_sequence/README.md)/[next>](./../DIR016_power_digit_sum/README.md) 

### The example:
`Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.`

<div align="center"><img alt="project-euler-lattice-paths" src="./p015.png" width="200px" height="auto"></div>

### The challenge:
`How many such routes are there through a 20×20 grid?`

### Initial thoughts:
At first glance this seems to fairly straightforward; however as soon as I tried to find a general pattern I would get lost. I could not figure out a way to methodically identify the paths for even a 4x4 grid. \
I ended up so badly lost that I eventually resorted to researching the problem online and finding that there is a general formula. There is also an interesting relationship to 
[Pascal's Triangle](https://en.wikipedia.org/wiki/Lattice_path#Combinations_and_NE_lattice_paths) 
which could be exploited in another solution. \
As it was I took the opportunity to try to learn about the basics of 
[binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient),
an area of mathematics I have not covered before, and to use the general formula shown in the article to calculate my solution. \
I also decided to keep the solution general so that rectangular grids could be used but square grids would be the default.

### Pseudocode for first iteration:
```
RECEIVE one OR two integer values
# these are the lengths of the sides of the grid
# if only one is given the second will be generated as being equal

SET y = one of the two integers
SET x = the other of the two integers
# the order here is not important

SET k = the smaller from x & y
SET n = the sum of x + y

CALCULATE n!/(k! * (n-k)!)
RETURN this solution
```

### Comments on first iteration:
Although it was somewhat disappointing to be unable to solve this challenge alone, the opportunity to learn a little about these new (to me) areas of mathematics was valuable. 

### Refactoring:
The formula ended up being very streamlined in the end so I think there is no need to refactor this time. 
