from math import factorial

def lattice_path_formula(x, y=None):
  if y is None: 
    y = x
  
  k = min([x, y])
  n = x + y

  path_possibilities = factorial(n)/(factorial(k) * factorial(n - k))
  return path_possibilities

if __name__ == '__main__':
  print(lattice_path_formula(20))
