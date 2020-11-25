sunday_first_count = 0
days_passed = 1
common_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_it_a_leap(year):
  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  elif year % 4 == 0:
    return True
  else:
    return False

def check_each_year():
  for year in range(1900, 2001):
    if is_it_a_leap(year):
      for month in leap_months:
        global days_passed 
        days_passed += month
        if days_passed % 7 == 0 and year > 1900:
          global sunday_first_count
          sunday_first_count += 1
    else:
      for month in common_months:
        days_passed += month
        if days_passed % 7 == 0 and year > 1900:
          sunday_first_count += 1
  return sunday_first_count

if __name__ == '__main__':
  print(check_each_year())
