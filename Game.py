import copy
from Player import Player
from Deck import Deck
from Hand import Hand

class Game():
  dealerLimit = 17
  softHit = True

  def __init__(self, players=[], dealer=None, deck=None):
    if not dealer:
      self.dealer = Player("Dealer")
    else:
      self.dealer = dealer
    self.originalPlayers = copy.copy(players)
    self.reset(deck)

  def reset(self, deck=None):
    if not deck:
      self.deck = Deck()
    self.round = 0
    self.players = self.originalPlayers
    for player in self.players:
      player.hand = Hand()

  def playGame(self):
    print self.deck.cards
    for _ in range(0, 2): #two cards to start
      self.dealer.hit(self.deck.dealOne())
      for player in self.players:
        print "player cards", player.hand.cards
        print "added one card"
        player.hit(self.deck.dealOne())
    self.playRound()

  def addPlayer(self, player):
    if self.round != 0:
      print "Cannot add a player until current game is finished"
      return
    self.originalPlayers.append(player)

  def playRound(self):
    self.round += 1
    print "Round " + str(self.round)
    remainingPlayers = []
    noHits = True
    for player in self.players:
      play = raw_input(player.name + ", your current hand is " + str(player.hand.cards) + ": hit? (y/n) ")
      if play.lower() == 'y':
        noHits = False
        player.hit(self.deck.dealOne())
        if player.hand.isBusted():
          print player.name, "has busted! Total:", player.hand.score()
        else:  
          remainingPlayers.append(player)
      else:
        remainingPlayers.append(player)
    self.players = remainingPlayers
    dealerScore = self.dealer.score()
    if dealerScore < self.__class__.dealerLimit or (dealerScore == self.__class__.dealerLimit and 1 in self.dealer.hand.cards):
      self.dealer.hit(self.deck.dealOne())
      noHits = False
    if noHits:
      winner = self.dealer
      winningScore = winner.score()
      for player in self.players:
        playerScore = player.score()
        if playerScore > winningScore:
          winningScore = playerScore
          winner = player
      newGame = raw_input(winner.name + " wins. Play again? Enter any key.")
      if newGame:
        self.reset()
        self.playGame()
      else:
        print "Goodbye!"    
    if len(self.players) <= 1:
      print "One or less players remaining:", len(self.players)
      winner = False
      if self.dealer.hand.isBusted():
        winner = self.players[0]
      elif not len(self.players):
        winner = self.dealer
      if winner:
        print "Hands at the end:"
        print self.dealer.name + ":", self.dealer.hand.cards
        for player in self.originalPlayers:
          print player.name + ":", player.hand.cards
        newGame = raw_input(winner.name + " wins. Play again? Enter any key.")
        if newGame:
          self.reset()
          self.playGame()
        else:
          print "Goodbye!"
      else: 
        self.playRound()
    else:
      self.playRound()  
