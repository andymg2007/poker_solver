import random
from poker.card import Card

class Deck:
    def __init__(self):
        self.cards = []

        ranks = [
            "2", "3", "4", "5", "6", "7", "8", 
            "9", "T", "J", "Q", "K", "A"
        ]

        suits = [
            "spades",
            "hearts",
            "diamonds",
            "clubs"
        ]

        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()