class Hand():
  def __init__(self, cards=None):
    if not cards:
      cards = []
    self.cards = cards
    print("hand cards array:", self.cards)

  def addCard(self, card):
    self.cards.append(card)

  def isBusted(self):
    return self.score() > 21

  def score(self):
    aceCount = 0
    total = 0
    for card in self.cards:
      if card == 1:
        aceCount += 1
      total += card
    while aceCount > 0:
      if total + 9 <= 21:
        aceCount -= 1
        total += 9
      else:
        break
    return total
