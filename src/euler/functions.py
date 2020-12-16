from math import floor, sqrt, ceil

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

# Originally from problem 008
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

# Originally from problem 016
def convert_int_to_digits(number):
  number_list = [int(i) for i in list(str(number))]
  return number_list

# Originally from problem 020
def sum_of_digits(large_number):
  result = sum(convert_int_to_digits(large_number))
  return result

# Originally from problem 021
def get_list_of_factors(number):
  list_of_factors = [1]
  if sqrt(number) % 1 == 0:
    list_of_factors.append(sqrt(number))

  for i in range((ceil(sqrt(number)))-1, 1, -1):
    if number % i == 0:
      list_of_factors.append(i)
      list_of_factors.append(number / i)
  if number == 0: return [0]
  if number == 1: return [1]
  return list_of_factors
