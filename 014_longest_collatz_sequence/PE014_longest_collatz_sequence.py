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
    number = next_collatz_term(number)
    counter += 1
  return counter

def actual_euler_problem(lim):
  longest_sequence = 0
  starting_number_with_longest_sequence = None
  for i in range(2, lim):
    sequence_length = how_many_collatz_terms(i)
    if sequence_length > longest_sequence:
      longest_sequence = sequence_length
      starting_number_with_longest_sequence = i
  return starting_number_with_longest_sequence

if __name__ == '__main__':
  print(actual_euler_problem(1000000))
