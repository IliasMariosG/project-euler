def sum_of_squares(max_number):
  total = 0
  for number in range(1, max_number+1):
    total += (number * number)
  return total

def square_of_sum(max_number):
  total_sum = 0
  for number in range(1, max_number+1):
    total_sum += number
  return total_sum * total_sum

def actual_euler_problem(number):
  answer = square_of_sum(number) - sum_of_squares(number)
  return answer

if __name__ == '__main__':
  print(actual_euler_problem(100))
  