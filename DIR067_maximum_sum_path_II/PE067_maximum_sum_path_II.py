problem_triangle_string_II = open("p067_triangle.txt")
problem_triangle_string_II = list(problem_triangle_string_II)
problem_triangle_list_of_lists = [line.split(' ') for line in problem_triangle_string_II]
problem_triangle_as_ints = \
[[int(strint) for strint in line] for line in problem_triangle_list_of_lists]

def remove_top_and_right_edge(triangle):
  new_smaller_triangle = []
  for idx in range(1, len(triangle)):
    new_smaller_triangle.append(triangle[idx][:-1])
  return new_smaller_triangle

def remove_top_and_left_edge(triangle):
  new_smaller_triangle = []
  for idx in range(1, len(triangle)):
    new_smaller_triangle.append(triangle[idx][1:])
  return new_smaller_triangle
  
def early_return_check(triangle):
  if len(triangle) < 2:
    return True

def memoisation_check(triangle):
  if str(triangle) in memoisation_cache:
    return True

def split_triangle(triangle):
  top = triangle[0][0]
  left_part = remove_top_and_right_edge(triangle)
  right_part = remove_top_and_left_edge(triangle)
  return (top, left_part, right_part)

def calculate_path_total(single_int, left_sum, right_sum):
  path_total = single_int + max([left_sum, right_sum])
  return path_total

def recursive_sum_path_calculation(triangle):
  if early_return_check(triangle):
    return triangle[0][0]

  if memoisation_check(triangle):
    return memoisation_cache[str(triangle)]

  top = split_triangle(triangle)[0]
  left_part = split_triangle(triangle)[1]
  right_part = split_triangle(triangle)[2]

  left_part = recursive_sum_path_calculation(left_part)
  right_part = recursive_sum_path_calculation(right_part)

  if type(left_part) is int and type(right_part) is int:
    path_sum = calculate_path_total(top, left_part, right_part)
    memoisation_cache[str(triangle)] = path_sum
    return path_sum

memoisation_cache = {}

if __name__ == '__main__':
  print(recursive_sum_path_calculation(problem_triangle_as_ints))
