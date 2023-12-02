import re
import sys

string_numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_numeric_string(string: str) -> str:
  if string.isdigit():
    return string
  
  return str(string_numbers.index(string))


with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

sum_part01 = 0
sum_part02 = 0

for line in file_lines:
  digits = re.findall(r'\d', line)
  sum_part01 += int(len(digits) and digits[0] + digits[-1])

  digits = re.findall(fr'(?=(\d|{"|".join(string_numbers)}))', line)
  sum_part02 += int(get_numeric_string(digits[0]) + get_numeric_string(digits[-1]))

print('Part01', sum_part01)
print('Part02', sum_part02)
