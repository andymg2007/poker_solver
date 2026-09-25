from poker.card import Card
from poker.hand import Hand


cards = [
    Card("A", "spades"),
    Card("A", "hearts"),
    Card("A", "diamonds"),
    Card("7", "clubs"),
    Card("7", "spades")
]

hand = Hand(cards)

print(hand.rank_counts())
print(hand.hand_rank())