import math
import sys


class Node:
  def __init__(self, line: str):
    splitted = line.split(' = (')
    self.name = splitted[0]

    splitted = splitted[1].split(', ')
    self.left = splitted[0]
    self.right = splitted[1][:-1]


def steps_part01() -> int:
  if not nodes.get('AAA'):
    return -1

  current_node: Node = nodes['AAA']
  steps = 0

  while True:
    for instruction in instructions:
      if current_node.name == 'ZZZ':
        return steps
      current_node = nodes[current_node.left if instruction == 'L' else current_node.right]
      steps += 1


def steps_part02() -> int:
  current_nodes = [node for node in nodes.values() if node.name.endswith('A')]
  steps = [0 for _ in range(len(current_nodes))]

  while len([x for x in current_nodes if not x.name.endswith('Z')]) > 0:
    for instruction in instructions:
      for ix, current_node in enumerate(current_nodes):
        if not current_node.name.endswith('Z'):
          current_nodes[ix] = nodes[current_node.left if instruction == 'L' else current_node.right]
          steps[ix] += 1

  # Luckily, the least common multiple (LCM) works :)
  return math.lcm(*steps)


with open(sys.argv[1]) as f:
  file_content = f.read()

splitted = file_content.split('\n\n')
instructions = splitted[0]

nodes = dict()

for node_line in splitted[1].splitlines():
  node = Node(node_line)
  nodes[node.name] = node

print('Part01', steps_part01())
print('Part02', steps_part02())
