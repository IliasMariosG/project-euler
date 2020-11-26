from math import factorial
from euler.functions import convert_int_to_digits
from euler.functions import sum_of_digits

def calculate_factorial(number):
  return factorial(number)

if __name__ == '__main__':
  print(
    sum_of_digits(
      calculate_factorial(
        100,
      )
    )
  )
