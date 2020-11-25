from math import factorial
from ./016_power_digit_sum/PE016_power_digit_sum import convert_int_to_digits

def calculate_factorial(number):
  return factorial(number)


if __name__ == '__main__':
  print(calculate_factorial(10))