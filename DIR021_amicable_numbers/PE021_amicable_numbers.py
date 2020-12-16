from euler.functions import get_list_of_factors

def check_if_amicable(number):
  if sum(get_list_of_factors(number)) == number: return False
  if sum(get_list_of_factors(sum(get_list_of_factors(number)))) == number:
    return True
  else:
    return False

def total_amicable_numbers_under(number):
  amicable_total = 0
  for i in range(number+1):
    if check_if_amicable(i):
      amicable_total += i
  return amicable_total

if __name__ == '__main__':
  print(total_amicable_numbers_under(10000))
