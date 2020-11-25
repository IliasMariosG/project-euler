def raise_x_to_n_th_power(x, n):
  return x**n

def convert_int_to_digits(number):
  number_list = [int(i) for i in list(str(number))]
  return number_list

def actual_euler_problem(x, n):
  result = sum(convert_int_to_digits(raise_x_to_n_th_power(x, n)))
  return result

if __name__ == '__main__':
  print(actual_euler_problem(2, 1000))
