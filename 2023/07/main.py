import sys

class Hand:
  CARDS_WORTH = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,  # in part02: 0
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    '1': 1,
  }

  def __init__(self, line: str):
    cols = line.split()
    self.cards = cols[0]
    self.bid = int(cols[1])

    self.worth_part01 = 0
    self.worth_part02 = 1

    card_counts = sorted([self.cards.count(c) for c in self.cards])
    jokers = self.cards.count('J')

    # Worth part01
    if 5 in card_counts:
      self.worth_part01 = 7
    elif 4 in card_counts:
      self.worth_part01 = 6
    elif 3 in card_counts:
      if 2 in card_counts:
        self.worth_part01 = 5
      else:
        self.worth_part01 = 4
    elif card_counts.count(2) == 4:
      self.worth_part01 = 3
    elif 2 in card_counts:
      self.worth_part01 = 2

    # Worth part02
    if jokers == 5:
      card_max_count = 0
    elif card_counts[-1] == jokers:
      card_max_count = card_counts[max(-(jokers + 1), -5)]
    else:
      card_max_count = card_counts[-1]

    if 5 == card_max_count + jokers:
      self.worth_part02 = 7
    elif 4 == card_max_count + jokers:
      self.worth_part02 = 6
    elif 3 == card_max_count + jokers:
      if card_max_count == 2:
        if card_counts.count(2) == 4:
          self.worth_part02 = 5
        else:
          self.worth_part02 = 4
      else:
        if 2 in card_counts and jokers != 2:
          self.worth_part02 = 5
        else:
          self.worth_part02 = 4
    elif card_counts.count(2) == 4 or (card_counts.count(2) == 2 and jokers == 1):
      self.worth_part02 = 3
    elif 2 == (card_max_count + jokers):
      self.worth_part02 = 2

  
  def __eq__(self, __value) -> bool:
    return __value.cards == self.cards
  
  def __lt__(self, other) -> bool:
    if self.worth == other.worth:
      for ix in range(len(self.cards)):
        s = self.CARDS_WORTH[self.cards[ix]]
        o = self.CARDS_WORTH[other.cards[ix]]
        if s == o:
          continue
        return s < o

    return self.worth < other.worth


with open(sys.argv[1]) as f:
  file_lines = f.read().splitlines()

hands = [Hand(line) for line in file_lines]
for hand in hands:
  hand.worth = hand.worth_part01
hands.sort()

result_part01 = 0
for ix, hand in enumerate(hands):
  result_part01 += hand.bid * (ix + 1)

result_part02 = 0
for hand in hands:
  hand.worth = hand.worth_part02
Hand.CARDS_WORTH['J'] = 0
hands.sort()

result_part02 = 0
for ix, hand in enumerate(hands):
  result_part02 += hand.bid * (ix + 1)

print('Part01', result_part01)
print('Part02', result_part02)
