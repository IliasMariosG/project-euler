def fib_gen(target, fib_seed=[1, 2]):
  fib_sequence = fib_seed
  while 1:
    next_fib_term = fib_sequence[-1] + fib_sequence[-2]
    if next_fib_term > target: break
    fib_sequence.append(next_fib_term)
  return fib_sequence

def list_sum_even(this_list):
  total = 0
  for i in this_list:
    if i % 2 == 0:
      total += i
  return total

def actual_euler_problem(target):
  print(list_sum_even(fib_gen(target)))

if __name__ == '__main__':
  actual_euler_problem(4000000)
