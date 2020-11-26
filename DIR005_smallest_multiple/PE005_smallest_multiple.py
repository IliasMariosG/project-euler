def smallest_multiple(max_number):
  candidate_multiple = max_number
  while 1:
    divisible_by_all = True
    for number in range(max_number, 0, -1):
      divisible_by_number = (candidate_multiple % number == 0)
      divisible_by_all = divisible_by_all and divisible_by_number
      if not divisible_by_all: break
    if divisible_by_all:
      return candidate_multiple
    else:
      candidate_multiple += max_number

if __name__ == '__main__':
  print(smallest_multiple(20))
