import sys

PRINT_MAP = True


class FieldType:
  DEFAULT = '.'
  PIPE = '_'
  ENCLOSED = 'I'
  NOT_ENCLOSED = 'O'


def get_start_position() -> tuple:
  for row_ix, line in enumerate(grid):
    for col_ix, c in enumerate(line):
      if c == 'S':
        grid[row_ix][col_ix] = 'F'
        return (row_ix, col_ix)

def get_pipe_length(row_ix: int, col_ix: int) -> int:
  length = 0

  while True:
    current_position = grid[row_ix][col_ix]
    normalized_grid[row_ix][col_ix] = ' '

    if current_position in ['|', 'L', 'J'] and normalized_grid[row_ix - 1][col_ix] == FieldType.DEFAULT:
      row_ix -= 1
    elif current_position in ['-', 'L', 'F'] and normalized_grid[row_ix][col_ix + 1] == FieldType.DEFAULT:
      col_ix += 1
    elif current_position in ['|', '7', 'F'] and normalized_grid[row_ix + 1][col_ix] == FieldType.DEFAULT:
      row_ix += 1
    elif current_position in ['-', 'J', '7'] and normalized_grid[row_ix][col_ix - 1] == FieldType.DEFAULT:
      col_ix -= 1
    else:
      return length

    length += 1

def mark_as_not_enclosed(row_ix: int, col_ix: int):
  if normalized_grid[row_ix][col_ix] != FieldType.DEFAULT:
    return

  normalized_grid[row_ix][col_ix] = FieldType.NOT_ENCLOSED

  if row_ix > 0:
    mark_as_not_enclosed(row_ix - 1, col_ix)
  if row_ix < len(normalized_grid) - 1:
    mark_as_not_enclosed(row_ix + 1, col_ix)
  if col_ix > 0:
    mark_as_not_enclosed(row_ix, col_ix - 1)
  if col_ix < len(normalized_grid[0]) - 1:
    mark_as_not_enclosed(row_ix, col_ix + 1)

def connected(p1: tuple, p2: tuple) -> bool:
  f = grid[p1[0]][p1[1]]  # Top or left item
  s = grid[p2[0]][p2[1]]  # Bottom or right item

  if p1[0] != p2[0]:
    # Vertical
    return f in ['|', '7', 'F'] and s in ['|', 'L', 'J']
  else:
    # Horizontal
    return f in ['-', 'L', 'F'] and s in ['-', 'J', '7']

def not_enclosed_in_loop(position: tuple, visited: list) -> bool:
  if position in visited:
    return False

  if position[0] == -1 or position[0] == len(grid) - 1 or position[1] == -1 or position[1] == len(grid[0]) - 1:
    return True

  visited.append(position)

  if not connected(position, (position[0], position[1] + 1)):
    if not_enclosed_in_loop((position[0] - 1, position[1]), visited):
      return True
  if not connected(position, (position[0] + 1, position[1])):
    if not_enclosed_in_loop((position[0], position[1] - 1), visited):
      return True
  if not connected((position[0] + 1, position[1]), (position[0] + 1, position[1] + 1)):
    if not_enclosed_in_loop((position[0] + 1, position[1]), visited):
      return True
  if not connected((position[0], position[1] + 1), (position[0] + 1, position[1] + 1)):
    if not_enclosed_in_loop((position[0], position[1] + 1), visited):
      return True

  return False


# The default limit of 1000 is not enough
sys.setrecursionlimit(1_000_000)

with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

grid = []
normalized_grid = []

for line in file_lines:
  grid.append([])
  normalized_grid.append([])
  for c in line:
    grid[-1].append(c)
    normalized_grid[-1].append(FieldType.DEFAULT)

start = get_start_position()
result_part01 = (get_pipe_length(*start) + 1) // 2
result_part02 = 0

for row_ix, line in enumerate(normalized_grid):
  for col_ix, c in enumerate(line):
    if c == FieldType.DEFAULT:
      if not_enclosed_in_loop((row_ix, col_ix), []):
        mark_as_not_enclosed(row_ix, col_ix)
      else:
        normalized_grid[row_ix][col_ix] = FieldType.ENCLOSED
        result_part02 += 1
  PRINT_MAP and print(''.join(line))

PRINT_MAP and print()

print('Part01', result_part01)
print('Part02', result_part02)
