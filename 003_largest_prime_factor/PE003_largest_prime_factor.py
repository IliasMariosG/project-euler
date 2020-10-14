def largest_prime_factor(number):
  numerator = number
  denominator = 2
  while numerator/denominator != 1:
    if numerator % denominator == 0:
      numerator = numerator/denominator
    else:
      denominator += 1
  return denominator

if __name__ == '__main__':
  print(largest_prime_factor(600851475143))
