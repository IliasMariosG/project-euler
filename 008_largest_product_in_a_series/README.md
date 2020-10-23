# Problem 008

## [Largest product in a series](https://projecteuler.net/problem=8)

[<prev](./../007_10001st_prime/README.md)/[next>](./../README.md) 

### The example:
`The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.`
```
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
```
`NB although presented on multiple lines, the above is to be treated as a single large integer.`

### The challenge:
`Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?`

### Initial thoughts:
I'm unable to think of any approach other than to systematically move through the number and check the product of each set of 13 digits. Continue to keep track of the largest observed product, and when the checking is finished, this will be the answer.

### Pseudocode for first iteration:
```
SET largest observed product = 0
CONVERT the large number to a list of single digits
FOR every digit except for the last twelve digits
  SLICE the list into a sub-list of thirteen digits
  CALCULATE the product of those thirteen digits
  IF the product is larger than the previous largest observed
  THEN update the largest observed product
  ELSE do nothing
RETURN the largest observed product
```

### Comments on first iteration:
The above method seems to work without any issue. After talking about the problem with others, there is one other possible method that may work. \
get the product of the first 13 digits. Then divide this by the first and multiply by the 14th, then continue to divide and multiply. This reduces the number of calculations significantly but introduces the issue of having to immediately skip over any 0s and presents the problem of an edge case where there are no sequences of 13 digits without containing a 0.

### Refactoring:
