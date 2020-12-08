# Problem 022

## [Names scores](https://projecteuler.net/problem=22)

[<prev](./../DIR021_amicable_numbers/README.md)/[next>](./../README.md) 

### The example:
`Using 
`[names.txt](https://projecteuler.net/project/resources/p022_names.txt), `
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.`

`For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.`

### The challenge:
`What is the total of all the name scores in the file?`

### Initial thoughts:
For this challenge I should find a way to extract the data from the `.txt` file through the code rather than copying and pasting the data into the `.py` file like I did [before](DIR067_maximum_sum_path_II/PE067_maximum_sum_path_II.py). This is something I've not done before but I'm certain there will be a solution. \
Other than this, the challenge is going to be fairly straightforward, a case of splitting the text into a list and sorting; then treating each name in turn with some logic to determine its points value. This will likely follow very similar logic to 
[this kata](https://www.codewars.com/kata/reviews/5bd866f5763340c483001a38/groups/5dc92bd85540590001232834) 
that I have done previously.

### Pseudocode for first iteration:
```
IMPORT the text from the given file
SPLIT the text into a list of names
SORT the list of names

PREPARE a dictionary where:
  k = letter (string)
  v = score (position in alphabet as integer)
  for all letters

FOR each name in the list
  SET name score = 0
  FOR each letter in the name
    ADD letter score to name score
  RETURN name score

SET overall list score = 0
FOR each name in list
  CALCULATE name position score = name score * position in list
  ADD name position score to overall list score
RETURN overall list score
```

### Comments on first iteration:
normal text

### Refactoring:
