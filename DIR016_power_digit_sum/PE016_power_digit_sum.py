from euler.functions import convert_int_to_digits
from euler.functions import sum_of_digits

def raise_x_to_n_th_power(x, n):
  return x**n

if __name__ == '__main__':
  print(
    sum_of_digits(
      raise_x_to_n_th_power(
        2,
        1000,
      )
    )
  )
