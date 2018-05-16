from Hand import Hand

class Player():
  var = 5
  def __init__(self, name, cards=None):
    self.name = name
    self.hand = Hand(cards)

  def hit(self, card):
    self.hand.addCard(card)

  def score(self):
    return self.hand.score()

"""
Left off having just changed method name for Player to hit (from addCard)
Could have inconsistencies, see error in left terminal
"""
