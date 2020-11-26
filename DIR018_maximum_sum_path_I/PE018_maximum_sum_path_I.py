example_triangle = [
  [3],
  [7,4],
  [2,4,6],
  [8,5,9,3]]

problem_triangle_string = """75
  95 64
  17 47 82
  18 35 87 10
  20 04 82 47 65
  19 01 23 75 03 34
  88 02 77 73 07 63 67
  99 65 04 28 06 16 70 92
  41 41 26 56 83 40 80 70 33
  41 48 72 33 47 32 37 16 94 29
  53 71 44 65 25 43 91 52 97 51 14
  70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
  04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

problem_triangle_list_of_strings = problem_triangle_string.split('\n')
problem_triangle_list_of_lists = [line.split(' ') for line in problem_triangle_list_of_strings]
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

  top = split_triangle(triangle)[0]
  left_part = split_triangle(triangle)[1]
  right_part = split_triangle(triangle)[2]

  left_part = recursive_sum_path_calculation(left_part)
  right_part = recursive_sum_path_calculation(right_part)

  if type(left_part) is int and type(right_part) is int:
    path_sum = calculate_path_total(top, left_part, right_part)
    return path_sum

if __name__ == '__main__':
  print(recursive_sum_path_calculation(problem_triangle_as_ints))
