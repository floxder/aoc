import functools
import operator
import sys


class Game:
  def __init__(self, line: str):
    line_splitted = line.split(': ')
    self.id = int(line_splitted[0].split(' ')[1])
    self.bags = []

    for bag in line_splitted[1].split('; '):
      self.bags.append({'red': 0, 'green': 0, 'blue': 0})

      for bag_item in bag.split(', '):
        bag_item_splitted = bag_item.split(' ')
        self.bags[-1][bag_item_splitted[1]] += int(bag_item_splitted[0])


with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

id_sum = 0
power_sum = 0

for line in file_lines:
  game = Game(line)

  game_possible = True
  max = {'red': 1, 'green': 1, 'blue': 1}

  for bag in game.bags:
    # Hardcoded values from the puzzle description
    if bag['red'] > 12 or bag['green'] > 13 or bag['blue'] > 14:
      game_possible = False

    for key in max:
      if bag[key] > max[key]:
        max[key] = bag[key]

  if game_possible:
    id_sum += game.id

  power_sum += functools.reduce(operator.mul, max.values(), 1)

print('Part01', id_sum)
print('Part02', power_sum)
