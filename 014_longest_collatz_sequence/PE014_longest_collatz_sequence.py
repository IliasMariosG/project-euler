def is_it_an_even(number):
  return number % 2 == 0

def next_collatz_term(number):
  if is_it_an_even(number):
    return number/2
  else:
    return 3 * number +1

def how_many_collatz_terms(number):
  counter = 1
  while number != 1:
    if number in collatz_cache:
      return counter + collatz_cache[number]
    else:
      number = next_collatz_term(number)
      counter += 1
  return counter

collatz_cache = {}

def actual_euler_problem(lim):
  longest_sequence = 0
  starting_number_with_longest_sequence = None
  for i in range(2, lim):
    sequence_length = how_many_collatz_terms(i)
    collatz_cache[i] = sequence_length
  return max(collatz_cache, key=lambda k: collatz_cache[k])

if __name__ == '__main__':
  print(actual_euler_problem(1000000))
