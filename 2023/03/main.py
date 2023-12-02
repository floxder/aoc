import functools
import operator
import sys


def get_number(line: str, ix: int) -> int | None:
  if ix < 0 or ix >= len(line) or not line[ix].isnumeric():
    return None

  number = line[ix]

  for c in reversed(line[:ix]):
    if c.isnumeric():
      number = c + number
    else:
      break

  for c in line[ix + 1:]:
    if c.isnumeric():
      number = number + c
    else:
      break
  
  return int(number)

def get_line_numbers(line: str, ix: int) -> list[int]:
  tmp = [get_number(line, ix) for ix in range(ix - 1, ix + 2)]

  if tmp[1] is None:
    return list(filter(lambda x: x is not None, tmp))
  else:
    return [tmp[1]]

def get_numbers_around(file_lines: list[str], row_ix: int, col_ix: int) -> list[int]:
  numbers = []

  if row_ix > 0:
    numbers.extend(get_line_numbers(file_lines[row_ix - 1], col_ix))
  if row_ix < len(file_lines):
    numbers.extend(get_line_numbers(file_lines[row_ix + 1], col_ix))
  
  tmp = get_number(file_lines[row_ix], col_ix - 1)
  if tmp is not None:
    numbers.append(tmp)

  tmp = get_number(file_lines[row_ix], col_ix + 1)
  if tmp is not None:
    numbers.append(tmp)

  return numbers


with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

sum_part01 = 0
sum_part02 = 0

for row_ix, line in enumerate(file_lines):
  for col_ix, c in enumerate(line):
    if not c.isnumeric() and c != '.':
      numbers = get_numbers_around(file_lines, row_ix, col_ix)
      sum_part01 += sum(numbers)

      if c == '*' and len(numbers) == 2:
        sum_part02 += functools.reduce(operator.mul, numbers, 1)

print('Part01', sum_part01)
print('Part02', sum_part02)
