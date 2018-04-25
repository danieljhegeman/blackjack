class Hand():
  def __init__(self, cards=None):
    if not cards:
      cards = []
    self.cards = cards
    print "hand cards array:", self.cards

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
      else:
        total += card
    tens = 0
    while aceCount > 0:
      if countNoAces + 10 + aceCount - 1 <= 21:
        aceCount -= 1
        total += 10
      else:
        break
    return total
