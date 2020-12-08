from math import sqrt, ceil

def add_one_number_triangle_fashion(this_list):
  if len(this_list) == 0:
    this_list.append(0)
  else:
    this_list.append(this_list[-1] + len(this_list))
  return this_list

def is_it_a_square(number):
  if sqrt(number) % 1 == 0:
    return True
  else:
    return False

def count_all_the_factors(number):
  total_factors = 0
  if is_it_a_square(number):
    total_factors += 1
  for i in range((ceil(sqrt(number)))-1, 0, -1):
    if number % i == 0:
      total_factors += 2
  return total_factors

def actual_euler_problem(looking_for_n_factors):
  this_list = []
  while 1:
    add_one_number_triangle_fashion(this_list)
    if count_all_the_factors(this_list[-1]) > looking_for_n_factors:
      return this_list[-1]

if __name__ == '__main__':
    print(actual_euler_problem(500))
