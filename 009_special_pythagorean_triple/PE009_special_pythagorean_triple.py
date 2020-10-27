def is_it_a_pythagorean_triple(list_of_three_ints):
  list_of_three_ints.sort()
  a = list_of_three_ints[0]
  b = list_of_three_ints[1]
  c = list_of_three_ints[2]
  if ((a * a) + (b * b)) == (c * c):
    return True
  else:
    return False

def find_three_numbers():
  for hyp in range(499, 0, -1):
    for opp in range(hyp-1, 0, -1):
      adj = 1000 - (hyp+opp)
      list_of_three_ints = [hyp, opp, adj]
      if is_it_a_pythagorean_triple(list_of_three_ints):
        return list_of_three_ints

def actual_euler_problem(list_of_three_ints):
  a = list_of_three_ints[0]
  b = list_of_three_ints[1]
  c = list_of_three_ints[2]
  return a * b * c

if __name__ == '__main__':
  print(actual_euler_problem(find_three_numbers()))
  