from PlayingCards import Deck
from PlayingCards import Card
from PlayingCards import Player

print("---Create New Deck----")
deck = Deck()
deck.show()

print("\n----Shuffle Deck----")
deck.shuffle()
deck.show()

print("\n----Draw First Card----")
card1 = deck.draw_card()
print("draw =", end=" ")
card1.show()

print("\n----Check Deck Again----")
deck.show()

print("\n----Draw Last Card----")
card2 = deck.draw_card(index=-1)
print("draw =", end=" ")
card2.show()

print("\n----Check Deck Again----")
deck.show()

print("\n----Create Player----")
player1 = Player("Ryan")
print("player1 = ", player1.name)

print("\n----Player1 Hand----")
player1.show()

print("\n----Player1 Draw 5 Cards----")
player1.draw(deck=deck, num_cards=5)

print("\n----Player1 Hand----")
player1.show()

print("\n----Deck-----")
deck.show()