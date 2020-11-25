from math import floor, sqrt

# Originally from problem 007
def sqrt_rounded_up(number):
  sqrt_rounded_up = floor(sqrt(number))+1
  return sqrt_rounded_up

def is_it_a_prime(number):
  if number == 2: return True
  if number % 2 == 0: return False
  for i in range(2, sqrt_rounded_up(number)+1):
    if number % i == 0:
      return False
  return True

# Originally from problem 007
def find_product_of_n_consecutive_digits(n, given_digits):
  product = 0
  starting_at = 0
  stopping_at = starting_at + n
  while stopping_at < len(given_digits):
    stopping_at = starting_at + n
    prod = 1
    for i in given_digits[starting_at:stopping_at]:
      prod *= i
    if prod > product:
      product = prod
    starting_at += 1
  return product
