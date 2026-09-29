from poker.card import Card
from poker.hand import Hand

cards = [
    Card("K", "spades"),
    Card("J", "spades"),
    Card("Q", "clubs"),
    Card("T", "spades"),
    Card("A", "spades")
]

hand = Hand(cards)

print(hand.hand_rank())