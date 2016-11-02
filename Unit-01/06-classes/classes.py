################################################
# Part 1

# What is a class?
# It is a blueprint of sorts that new objects can be created from.

# What is an instance?
# An object created from a specified class

# What is inheritance?
# When a class inherits from another class. The inheriting class then be able to access the same properties and methods from the parent class.

# What is multiple inheritance?
# Same as above but the child class inherits from multiple parent classes

# What is polymorphism?
# In a situation of inheritance or multiple inheritance, the child class can implement its own version of a method(s) it inherits from a parent class.

# What is method resolution order or MRO?
# It is the order of location/classes in which is searched to find a method associated to an object/instance. Usually starting from the initial class from which an object is created then going up to each successive parent it inherits from


################################################
# Part 2

import random

class Deck():
	def __init__(self):
		self.cards_in_deck = []
		self.cards_out_of_play = []

		suits = ("Hearts","Diamonds","Clubs","Spades")
		values = ("A","2","3","4","5","6","7","8","9","10","J","Q","K")
		for s in range(0,4):
			for v in range(0,13):
				card = Card(suits[s], values[v])
				self.cards_in_deck.append(card)

	# def __str__(self):
	# 	for card in self.cards_in_deck:
	# 		print(card.suit, card.value)
	# get an error from this for some reason

	def print_deck(self):
		print("Cards in the deck:")
		for card in self.cards_in_deck:
			print(card.suit, card.value)

	def print_out_of_play(self):
		print("Cards out of play:")
		for card in self.cards_out_of_play:
			print(card.suit, card.value)

	def deal(self):
		dealt_card = self.cards_in_deck.pop(0)
		print("Card dealt: " + dealt_card.suit, dealt_card.value)
		self.cards_out_of_play.append(dealt_card)
		

	def shuffle(self):
		random.shuffle(self.cards_in_deck)
		random.shuffle(self.cards_in_deck)


class Card():
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value



deck = Deck()
deck.print_deck()
deck.shuffle()
deck.print_deck()







