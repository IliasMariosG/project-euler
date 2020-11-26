from euler.functions import is_it_a_prime

def list_o_primes(length):
  list_o_primes = []
  i = 2
  while len(list_o_primes) < length:
    if is_it_a_prime(i):
      list_o_primes.append(i)
    i += 1
  return list_o_primes

def actual_euler_problem(n_th):
  return list_o_primes(n_th)[-1]

if __name__ == '__main__':
  print(actual_euler_problem(10001))
