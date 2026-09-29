from collections import Counter

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def rank_counts(self):
        return Counter(card.rank for card in self.cards)

    def rank_values(self):
        rank_map = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        values = []
        for card in self.cards:
             values.append(rank_map[card.rank])
        return values
    
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

    def is_straight(self, values):
        is_normal_straight = True
        is_low_straight = True

        sorted_values = sorted(values)
        low_values = values.copy()
        if 14 in low_values:
            ace_index = low_values.index(14)
            low_values[ace_index] = 1
        low_values.sort()

        for value in range(len(sorted_values)-1):
            if sorted_values[value+1] - sorted_values[value] != 1:
                is_normal_straight = False
        if is_normal_straight: return True
        if 1 in low_values:
            for i in range(len(low_values)-1):
                if low_values[i+1] - low_values[i] != 1:
                    is_low_straight = False
            if is_low_straight: return True
        return False

    def is_flush(self):
        counts = Counter(card.suit for card in self.cards)
        return 5 in counts.values()

    def hand_rank(self):
        counts = self.rank_counts()
        values = self.rank_values()

        if self.is_straight(values) and self.is_flush():
            return "Straight Flush"

        if self.is_four_of_a_kind():
            return "Four of a Kind"

        if self.is_full_house():
            return "Full House"

        if self.is_flush():
            return "Flush"

        if self.is_straight(values):
            return "Straight"

        if 3 in self.is_three_of_a_kind():
            return "Three of a Kind"

        if self.is_two_pair():
            return "Two Pair"

        if 2 in self.is_pair():
            return "Pair"

        return "High Card"