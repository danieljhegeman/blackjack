from random import randint

class Deck(): 
  def __init__(self, cards=None): 
    if cards: 
      self.cards = cards 
    else: 
      self.cards = self.generateDeck()
    print("cards in deck:", self.cards)
    self.shuffle()
    self.shuffle()
    print("shuffled deck:", self.cards)
 
  def generateDeck(self): 
    cards = [] 
    for suit in range(4): 
      for card in range(1, 11): 
        if card == 10: 
          for _ in range(4): 
            cards.append(card) 
        else: 
          cards.append(card) 
    return cards 

  def shuffle(self): 
    shuffled = [] 
    cards = self.cards 
    while len(cards): 
      index = randint(0, len(cards) - 1)  
      shuffled.append(cards[index]) 
      if index == len(cards) - 1: 
        cards = cards[0:index - 1] 
      else: 
        first = cards[0:index] 
        first.extend(cards[index + 1:])
        cards = first
    self.cards = shuffled

  def dealOne(self):
    return self.cards.pop()
