from math import sqrt, ceil

def get_list_of_factors(number):
  list_of_factors = [1]
  if sqrt(number) % 1 == 0:
    list_of_factors.append(sqrt(number))

  for i in range((ceil(sqrt(number)))-1, 1, -1):
    if number % i == 0:
      list_of_factors.append(i)
      list_of_factors.append(number / i)
  return list_of_factors

if __name__ == '__main__':
  print(get_list_of_factors(144))
