import random


class Deck:

    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for j in range(1, 14):
                self.cards.append(Card(i, j))

    def show(self):
        for card in self.cards:
            card.show()

    # Fisher Yates Shuffle, every card has equal chance of being chosen.
    # Pick 1 from all 52, then 1 from remaining 51....
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self, index=0):
        return self.cards.pop(index)


class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num_cards=1):
        for i in range(num_cards):
            self.hand.append(deck.draw_card())

    def show(self):
        for i in self.hand:
            print("{} of {}".format(i.val, i.suit))