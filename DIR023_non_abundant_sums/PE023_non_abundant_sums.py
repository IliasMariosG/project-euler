from euler.functions import get_list_of_factors

def is_it_abundant_or_not(number):
  if sum(get_list_of_factors(number)) > number:
    return True
  else:
    return False

def find_all_abundant_numbers_below(limit):
  list_of_abundants = []
  for i in range(limit):
    if is_it_abundant_or_not(i):
      list_of_abundants.append(i)
  return list_of_abundants

def check_if_number_can_be_expressed_as_sum_of_two_list_elements(number, list):
  for i in list:
    if (number - i) in list:
      return True
  return False

def calculate_sum_of_all_numbers_below_limit_that_cannot_be_expressed_as_sum_of_two_abundants(
  limit
):
  list_of_abundants = find_all_abundant_numbers_below(limit)
  list_of_cannot_be_expressed_as_sum = []
  for i in range(limit):
    if not check_if_number_can_be_expressed_as_sum_of_two_list_elements(i, list_of_abundants):
      list_of_cannot_be_expressed_as_sum.append(i)
  return sum(list_of_cannot_be_expressed_as_sum)

if __name__ == '__main__':
  print(calculate_sum_of_all_numbers_below_limit_that_cannot_be_expressed_as_sum_of_two_abundants(28123))
