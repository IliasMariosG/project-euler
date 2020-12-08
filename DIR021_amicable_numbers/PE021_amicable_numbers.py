from math import sqrt, ceil

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
