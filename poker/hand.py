from collections import Counter

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def rank_counts(self):
        return Counter(card.rank for card in self.cards)

    def is_pair(self):
        counts = self.rank_counts()

        return 2 in counts.values()

    def is_two_pair(self):
        counts = self.rank_counts()
        return list(counts.values()).count(2) == 2

    def is_three_of_a_kind(self):
        counts = self.rank_counts()
        return 3 in counts.values()

    def is_four_of_a_kind(self):
        counts = self.rank_counts()
        return 4 in counts.values()

    def is_full_house(self):
        counts = self.rank_counts()
        return 3 in counts.values() and 2 in counts.values()

    def hand_rank(self):
        counts = self.rank_counts()

        if 4 in counts.values():
            return "Four of a Kind"

        if 3 in counts.values() and 2 in counts.values():
            return "Full House"

        if 3 in counts.values():
            return "Three of a Kind"

        if list(counts.values()).count(2) == 2:
            return "Two Pair"

        if 2 in counts.values():
            return "Pair"

        return "High Card"