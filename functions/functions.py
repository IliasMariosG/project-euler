# from math import floor, sqrt

# # Originally from problem 007
# def sqrt_rounded_up(number):
#   sqrt_rounded_up = floor(sqrt(number))+1
#   return sqrt_rounded_up

# def is_it_a_prime(number):
#   if number == 2: return True
#   if number % 2 == 0: return False
#   for i in range(2, sqrt_rounded_up(number)+1):
#     if number % i == 0:
#       return False
#   return True
