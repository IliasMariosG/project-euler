def multiples_of_x_up_to(max_number, x):
  total = 0
  counter = 0
  while counter < max_number:
    total += counter
    counter += x
  return total

def actual_euler_problem(max_number, x, y):
  total = multiples_of_x_up_to(max_number, x) + multiples_of_x_up_to(max_number, y) - multiples_of_x_up_to(max_number, x*y)
  return total

if __name__ == '__main__':
  print(actual_euler_problem(1000, 3, 5))
