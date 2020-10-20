from math import floor, sqrt

def sqrt_rounded_up(number):
  sqrt_rounded_up = floor(sqrt(number))+1
  return sqrt_rounded_up

def is_it_a_prime(number):
  if number == 2: return True
  if number % 2 == 0: return False
  for i in range(2, sqrt_rounded_up(number)+1):
    if number % i == 0:
      return False
  return True

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
