import re
import sys


class MapInfo:
  def __init__(self, line: str):
    self.dst, self.src, self.length = [int(x) for x in line.split()]


class Map:
  def __init__(self, to_parse: str):
    self.map_info = [MapInfo(line) for line in to_parse.splitlines()[1:]]

  def map(self, number: int) -> int:
    for map_info in self.map_info:
      diff = number - map_info.src
      if 0 <= diff <= map_info.length:
        return map_info.dst + diff
    return number

  def map_reverse(self, number: int) -> int:
    for map_info in self.map_info:
      diff = number - map_info.dst
      if 0 <= diff <= map_info.length:
        return map_info.src + diff
    return number


class SeedRange:
  def __init__(self, line: str):
    self.start, length = (int(x) for x in line.split())
    self.end = self.start + length


def get_min_location_part01() -> int:
  for location in range(1_000_000_000):
    item_to_map = location
    for map in reversed(maps):
      item_to_map = map.map_reverse(item_to_map)
    
    for seed_range in seed_ranges:
      if seed_range.start <= item_to_map < seed_range.end:
        return location

  return -1


with open(sys.argv[1]) as f:
  file_content = f.read()


splitted = file_content.split('\n\n')
seeds = [int(seed) for seed in splitted[0].split()[1:]]
maps = [Map(map) for map in splitted[1:]]

locations = set()
seed_ranges = {SeedRange(x) for x in re.findall(r'[^ ]+ [^ ]+', splitted[0].split(': ')[1])}

for item_to_map in seeds:
  item_to_map = item_to_map
  for map in maps:
    item_to_map = map.map(item_to_map)
  locations.add(item_to_map)

print('Part01', min(locations))
print('Part02', get_min_location_part01())
