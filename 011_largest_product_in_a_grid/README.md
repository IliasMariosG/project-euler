# Problem 011

## [Largest product in a grid](https://projecteuler.net/problem=11)

[<prev](./../010_summation_of_primes/README.md)/[next>](./../012_highly_divisible_triangular_number/README.md) 

### The example:
`In the 20×20 grid below, four numbers along a diagonal line have been marked in red and/or bold (depending on rendering).`\
<details>
  <summary>
    Show/hide grid
  </summary>

  |||||||||||||||||||||
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  |08|02|22|97|38|15|00|40|00|75|04|05|07|78|52|12|50|77|91|08|
  |49|49|99|40|17|81|18|57|60|87|17|40|98|43|69|48|04|56|62|00|
  |81|49|31|73|55|79|14|29|93|71|40|67|53|88|30|03|49|13|36|65|
  |52|70|95|23|04|60|11|42|69|24|68|56|01|32|56|71|37|02|36|91|
  |22|31|16|71|51|67|63|89|41|92|36|54|22|40|40|28|66|33|13|80|
  |24|47|32|60|99|03|45|02|44|75|33|53|78|36|84|20|35|17|12|50|
  |32|98|81|28|64|23|67|10|<span style="color: red;">**26**</span>|38|40|67|59|54|70|66|18|38|64|70|
  |67|26|20|68|02|62|12|20|95|<span style="color: red;">**63**</span>|94|39|63|08|40|91|66|49|94|21|
  |24|55|58|05|66|73|99|26|97|17|<span style="color: red;">**78**</span>|78|96|83|14|88|34|89|63|72|
  |21|36|23|09|75|00|76|44|20|45|35|<span style="color: red;">**14**</span>|00|61|33|97|34|31|33|95|
  |78|17|53|28|22|75|31|67|15|94|03|80|04|62|16|14|09|53|56|92|
  |16|39|05|42|96|35|31|47|55|58|88|24|00|17|54|24|36|29|85|57|
  |86|56|00|48|35|71|89|07|05|44|44|37|44|60|21|58|51|54|17|58|
  |19|80|81|68|05|94|47|69|28|73|92|13|86|52|17|77|04|89|55|40|
  |04|52|08|83|97|35|99|16|07|97|57|32|16|26|26|79|33|27|98|66|
  |88|36|68|87|57|62|20|72|03|46|33|67|46|55|12|32|63|93|53|69|
  |04|42|16|73|38|25|39|11|24|94|72|18|08|46|29|32|40|62|76|36|
  |20|69|36|41|72|30|23|88|34|62|99|69|82|67|59|85|74|04|36|16|
  |20|73|35|29|78|31|90|01|74|31|49|71|48|86|81|16|23|57|05|54|
  |01|70|54|71|83|51|54|69|16|92|33|48|61|43|52|01|89|19|67|48|
</details>

`The product of these numbers is 26 × 63 × 78 × 14 = 1788696.`

### The challenge:
`What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?`

### Initial thoughts:
This looks like a 2D version of the previous 
[Problem 008](./../008_largest_product_in_a_series).
It will follow a similar pattern but with extra functionality to accound for the differing directions needed to be checked.\
This is also a good opportunity to be introduced to NumPy, which can be used to manipulate and iterate through 2-dimentional arrays of numbers. 

### Pseudocode for first iteration:

```
USE numpy
USE function from Problem 008

CONVERT given 20x20 grid into a numpy array
```
</details>
<details>
  <summary>
    Find max product in the rows
  </summary>

  ```
  SET max row product = 0
  FOR each row in the array
    FIND the largest product of 4 consecutive numbers
    IF this product is larger than max row product
    THEN update max row product to the new max
    ELSE do nothing
  RETURN max row product
  ```
</details>

<details>
  <summary>
    Find max product in the columns
  </summary>

  ```
  TRANSPOSE the array
  PERFORM find max product in the rows
  RETURN max col product
  ```
</details>

<details>
  <summary>
    Find max product in diagonals I (top-left to bottom-right)
  </summary>

  ```
  DEFINE what a diagonal is
    SET the starting point of the diagonal
      FOUR times
        MOVE down one row
        MOVE left one column
    
  SET max diag product = 0  
  FOR every number in the grid that can be the start of a diagonal
  # ie not the bottom three rows or the right three columns
    FIND the product of the four-digit diagonal
    IF this product is larger than max diag product
    THEN update max diag product to the new max
    ELSE do nothing
  RETURN max diag product1
  ```
</details>

<details>
  <summary>
    Find max product in diagonals II (top-right to bottom-left)
  </summary>

  ```
  FLIP the array using x OR y axis
  PERFORM find max diagonal product I
  RETURN max diag product2
  ```
</details>

```
SELECT the largest number from the four calculated maximums
RETURN this as the solution
```

### Comments on first iteration:
The above set of functions provided the solution as expected. This was an interesting exercise in beginning to experiment with NumPy and to explore and understand some of the possibilities of working with it.

### Refactoring:
