def is_palindrome(number):
  str_number = str(number)
  rev_str_no = str_number[::-1]
  if str_number == rev_str_no:
    return True
  else:
    return False

def find_high_product(max_number, min_number):
  palindrome_collection = []
  for i in range(max_number, min_number-1, -1):
    for j in range(max_number, i-1, -1):
      if is_palindrome(i * j):
        palindrome_collection.append(i*j)
  return max(palindrome_collection)

if __name__ == '__main__':
  print(find_high_product(999, 100))
