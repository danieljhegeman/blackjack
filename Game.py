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
    self.deck = deck
    self.round = 0

  def reset(self, deck=None):
    if not deck:
      self.deck = Deck()
    self.round = 0
    self.players = self.originalPlayers
    for player in self.players:
      player.hand = Hand()
    self.dealer.hand = Hand()

  def playGame(self):
    self.reset()
    for _ in range(0, 2): #two cards to start
      self.dealer.hit(self.deck.dealOne())
      for player in self.players:
        player.hit(self.deck.dealOne())
    for player in self.players:
      print(player.name + "\'s hand:", player.hand.cards)
    print(self.dealer.name + "\'s hand:", self.dealer.hand.cards)
    self.playRound()

  def addPlayer(self, player):
    if self.round != 0:
      print("Cannot add a player until current game is finished")
      return
    self.originalPlayers.append(player)

  def playerTurn(self, player):
    play = input(player.name + ", your current hand is " + str(player.hand.cards) + ": hit? (y/n) ")
    if play.lower() == 'y':
      self.noHits = False
      player.hit(self.deck.dealOne())
      print(player.name + "\'s hand:", player.hand.cards)
      if player.hand.isBusted():
        print(player.name, "has busted! Total:", player.score())
      else:
        self.remainingPlayers.append(player)
    else:
      self.remainingPlayers.append(player)

  def dealerTurn(self):
    dealerScore = self.dealer.score()
    if dealerScore < self.__class__.dealerLimit or (dealerScore == self.__class__.dealerLimit and 1 in self.dealer.hand.cards):
      self.dealer.hit(self.deck.dealOne())
      print(self.dealer.name + "\'s hand:", self.dealer.hand.cards)
      self.noHits = False
      if self.dealer.hand.isBusted():
        print(self.dealer.name, "has busted! Total:", self.dealer.score())
    
  def playRound(self):
    self.round += 1
    print("Round " + str(self.round))
    self.remainingPlayers = []
    self.noHits = True
    for player in self.players:
      self.playerTurn(player)
    self.players = self.remainingPlayers
    self.dealerTurn()
    if self.noHits:
      self.handleScores()
    else:
      self.playRound()

  def handleScores(self):
    winner = self.dealer
    if self.dealer.hand.isBusted():
      winningScore = 0
    else:
      winningScore = winner.score()
    for player in self.players:
      playerScore = player.score()
      if playerScore > winningScore:
        winningScore = playerScore
        winner = player
    print(winner.name + " wins.")
    print("Hands at the end:")
    print(self.dealer.name + ":", self.dealer.hand.cards)
    for player in self.originalPlayers:
      print(player.name + ":", player.hand.cards)
    newGame = input(winner.name + " wins. Play again? Enter any key.")
    if newGame:
      self.playGame()
    else:
      print("Goodbye!")
