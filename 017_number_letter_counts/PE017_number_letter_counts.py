def how_many_letters_1_to_19(n):
  letter_count_dict_1_to_19 = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8} 
  return letter_count_dict_1_to_19[n]

def how_many_letters_10s_less_than_100(n):
  letter_count_dict_10s_to_90 = {
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6}
  return letter_count_dict_10s_to_90[n]

def how_many_letters_20_to_99(n):
  if n % 10 == 0:
    return how_many_letters_10s_less_than_100(n)
  else:
    tens = n // 10 * 10
    units = n - tens
    return how_many_letters_10s_less_than_100(tens) + how_many_letters_1_to_19(units)

def how_many_letters_1_to_99(n):
  if n <= 19:
    return how_many_letters_1_to_19(n)
  else:
    return how_many_letters_20_to_99(n)

def how_many_letters_100s_less_than_1000(n):
  hundred = 7
  return how_many_letters_1_to_19(int(n / 100)) + hundred

def how_many_letters_100_to_999(n):
  hundred_and = 10
  if n % 100 == 0:
    return how_many_letters_100s_less_than_1000(n)
  else:
    return how_many_letters_1_to_19(n //100) + hundred_and + how_many_letters_1_to_99(n % 100)

def how_many_letters_1_to_1000(n):
  if n <= 99:
    return how_many_letters_1_to_99(n)
  elif n <= 999:
    return how_many_letters_100_to_999(n)
  elif n == 1000:
    return 11

def actual_euler_problem(n):
  total_letters = 0
  for i in range(1, n+1):
    letters = how_many_letters_1_to_1000(i)
    total_letters += letters
  return total_letters

if __name__ == '__main__':
  print(actual_euler_problem(1000))
