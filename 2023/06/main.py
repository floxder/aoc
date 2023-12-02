import functools
import operator
import sys


class Race:
  def __init__(self, time: int, distance: int):
    self.time = time
    self.distance = distance
    self.possible_ways = 0

  def win_possible(self, hold_time: int) -> bool:
    speed = hold_time
    time_left = self.time - hold_time

    traveled_distance = speed * time_left
    return traveled_distance > self.distance
    

with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

time_items = file_lines[0].split()[1:]
distance_items = file_lines[1].split()[1:]

times = [int(time) for time in time_items] + [int(''.join(time_items))]
distances = [int(distance) for distance in distance_items] + [int(''.join(distance_items))]

races = [Race(times[ix], int(distances[ix])) for ix in range(len(times))]

possible_ways = []

for race in races:
  possible_ways.append(0)
  for hold_time in range(1, race.time + 1):
    if race.win_possible(hold_time):
      possible_ways[-1] += 1

result_part01 = functools.reduce(operator.mul, possible_ways[:-1], 1)
result_part02 = possible_ways[-1]

print('Part01', result_part01)
print('Part02', result_part02)
