big_txt_of_names = open("p022_names.txt")
big_list_of_names = list(big_txt_of_names)
big_list_of_names = big_list_of_names[0].split(',')
big_list_of_names = sorted(big_list_of_names)

alphabet_dict = {
  "A": 1,
  "B": 2,
  "C": 3,
  "D": 4,
  "E": 5,
  "F": 6,
  "G": 7,
  "H": 8,
  "I": 9,
  "J": 10,
  "K": 11,
  "L": 12,
  "M": 13,
  "N": 14,
  "O": 15,
  "P": 16,
  "Q": 17,
  "R": 18,
  "S": 19,
  "T": 20,
  "U": 21,
  "V": 22,
  "W": 23,
  "X": 24,
  "Y": 25,
  "Z": 26,
  }

def convert_name_into_score(name):
  name_split = list(name)
  name_score = 0
  for letter in name_split:
    if letter in alphabet_dict:
      name_score += alphabet_dict[letter]
  return name_score

def convert_list_of_names_to_scores(list_of_names):
  list_of_scores = []
  for name in list_of_names:
    list_of_scores.append(convert_name_into_score(name))
  return list_of_scores

def calculate_overall_list_score(list_of_scores):
  new_list_of_scores = [None] + list_of_scores
  overall_list_score = 0
  for idx, score in enumerate(new_list_of_scores):
    if type(score) is int:
      overall_list_score += idx * score
  return overall_list_score

if __name__ == '__main__':
  print(calculate_overall_list_score(
    convert_list_of_names_to_scores(
      big_list_of_names
    )
  ))
