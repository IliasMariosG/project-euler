from euler.functions import is_it_a_prime

def all_primes_under(limit):
  prime_list = []
  for n in range(2, limit):
    if is_it_a_prime(n):
      prime_list.append(n)
  return prime_list

def sum_a_list(list):
  return sum(list)

def actual_euler_problem(limit):
  return sum_a_list(all_primes_under(limit))

if __name__ == '__main__':
  print(actual_euler_problem(2000000))
