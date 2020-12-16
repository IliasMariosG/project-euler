from euler.functions import get_list_of_factors

def is_it_abundant_or_not(number):
  if sum(get_list_of_factors(number)) > number:
    return True
  else:
    return False


if __name__ == '__main__':
  # print(is_it_abundant_or_not(28))