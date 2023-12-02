import functools
import sys


JUMP_SIZE = 1


class Pair:
  def __init__(self, position: tuple, other_positions: list[tuple]):
    self.position = position
    distances = [self.row_distance(o) + self.col_distance(o) for o in other_positions]
    self.distances_sum = sum(distances)
  
  def row_distance(self, other_position: tuple) -> int:
    row_ix_max = max(other_position[0], self.position[0])
    row_ix_min = min(other_position[0], self.position[0])

    jumps = len([True for row in map[row_ix_min + 1:row_ix_max] if '.' not in row])

    return abs(other_position[0] - self.position[0]) - jumps + jumps * JUMP_SIZE

  def col_distance(self, o: tuple) -> int:
    col_ix_min = min(o[1], self.position[1])
    col_ix_max = max(o[1], self.position[1])

    jumps = len([True for col_ix in range(col_ix_min, col_ix_max) if map[0][col_ix] == JUMP_SIZE])

    return abs(o[1] - self.position[1]) - jumps + jumps * JUMP_SIZE


with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

results = []

for jump_size in [2, 1_000_000]:
  JUMP_SIZE = jump_size

  map = []

  for line in file_lines:
    chars = [c for c in line]
    if '#' in line:
      map.append(chars.copy())
    else:
      map.append([JUMP_SIZE for _ in line])

  col_ix = 0
  while col_ix < len(map[0]):
    col = [True for row_ix in range(len(map)) if map[row_ix][col_ix] == '#']
    if len(col) == 0:
      for row_ix in range(len(map)):
        map[row_ix][col_ix] = JUMP_SIZE
      col_ix += 1
    col_ix += 1

  pairs = []
  for row_ix, line in enumerate(map):
    for col_ix, c in enumerate(map[row_ix]):
      if c == '#':
        other = []
        for tmp_row_ix, _ in enumerate(map):
          for tmp_col_ix, _ in enumerate(map[row_ix]):
            if (tmp_row_ix == row_ix and tmp_col_ix > col_ix or tmp_row_ix > row_ix) and map[tmp_row_ix][tmp_col_ix] == '#':
              other.append((tmp_row_ix, tmp_col_ix))
        pairs.append(Pair((row_ix, col_ix), other))
    
  results.append(functools.reduce(lambda sum, pair: sum + pair.distances_sum, pairs, 0))

print('Part01', results[0])
print('Part02', results[1])
