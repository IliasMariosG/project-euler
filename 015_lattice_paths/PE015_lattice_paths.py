def get_path_length(grid_side):
  return 2* grid_side

def raise_2_to_the_power_of(n):
  return 2**n

def convert_number_to_binary(number):
  return bin(number)[2:]

def pad_binary_with_leading_zeroes(number_str, padding):
  return number_str.zfill(padding)

def split_string_into_characters(this_str):
  this_str = list(this_str)
  return this_str

def convert_str_bin_digits_to_int_ones_and_minus_ones(string_binary_digits):
  list_ones_and_neg_ones = [1 if i == "1" else -1 for i in string_binary_digits]
  return list_ones_and_neg_ones

def how_many_valid_paths(this_list_of_lists):
  counter = 0
  for sub_list in this_list_of_lists:
    if sum(sub_list) == 0:
      counter += 1
  return counter

def make_list_of_binary_numbers(lim):
  list_of_binaries = []
  for i in range(lim):
    list_of_binaries.append(bin(i)[2:])
  return list_of_binaries

def actual_euler_problem(grid_side):
  path_length = get_path_length(grid_side)
  possible_paths = raise_2_to_the_power_of(path_length)
  all_path_possibilities = make_list_of_binary_numbers(possible_paths)
  all_path_possibilities = [pad_binary_with_leading_zeroes(path, path_length) for path in all_path_possibilities]
  all_path_possibilities = [split_string_into_characters(path) for path in all_path_possibilities]
  all_path_possibilities = [convert_str_bin_digits_to_int_ones_and_minus_ones(path) for path in all_path_possibilities]
  solution = how_many_valid_paths(all_path_possibilities)
  return solution

from math import factorial

def lattice_path_formula(x, y=None):
  if y is None: 
    y = x
  
  k = min([x, y])
  n = x + y

  path_possibilities = factorial(n)/(factorial(k) * factorial(n - k))
  return path_possibilities

if __name__ == '__main__':
  print(lattice_path_formula(20))
  # print(actual_euler_problem(20))
