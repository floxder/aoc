import sys


class History:
  def __init__(self, line: str):
    self.sequences = [[int(x) for x in line.split()]]

    while self.sequences[-1][-1] or self.sequences[-1][-2] or self.sequences[-1][0] or self.sequences[-1][1]:
      self.sequences.append(
        [self.sequences[-1][ix] - self.sequences[-1][ix - 1] for ix in range(1, len(self.sequences[-1]))]
      )

    self.sequences[-1].append(0)
    self.sequences[-1].insert(0, 0)

    for ix in range(len(self.sequences) - 2, -1, -1):
      self.sequences[ix].append(self.sequences[ix][-1] + self.sequences[ix + 1][-1])
      self.sequences[ix].insert(0, self.sequences[ix][0] - self.sequences[ix + 1][0])


with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

sum_end = 0
sum_start = 0

for line in file_lines:
  history = History(line)
  sum_end += history.sequences[0][-1]
  sum_start += history.sequences[0][0]

print('Part01', sum_end)
print('Part02', sum_start)
