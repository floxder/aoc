import sys


class Card:
  cards = {}

  def __init__(self, line: str):
    splitted = line.split(': ')
    self.id = int(splitted[0].split()[1])
    list_of_nums = splitted[1].split(' | ')

    self.winning_numbers = [int(num) for num in list_of_nums[0].split() if num.isnumeric()]
    self.available_numbers = [int(num) for num in list_of_nums[1].split() if num.isnumeric()]
    
    self.matches = len(list(filter(lambda num: num in self.winning_numbers, self.available_numbers)))
    self.worth = self.matches and 2 ** (self.matches - 1)

    card = Card.cards.get(self.id)
    Card.cards[self.id] = (card or 0) + 1

    for card_id in range(self.id + 1, self.id + 1 + self.matches):
      card = Card.cards.get(card_id)
      Card.cards[card_id] = (card or 0) + Card.cards[self.id]


with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

sum_part01 = 0

for line in file_lines:
  card = Card(line)
  sum_part01 += card.worth

sum_part02 = sum(Card.cards.values())

print('Part01', sum_part01)
print('Part02', sum_part02)
