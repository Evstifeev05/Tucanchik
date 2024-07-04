from Card import Card


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)

    def score(self, hands=None):
        summ = 0
        cards = list(map(str, self.cards))
        for c in set(cards):
            leader = False
            count_cards = cards.count(c)
            if c in Card.CARD_SPEC and hands is not None:
                leader = (max([list(map(str, hand.cards)).count(c) for hand in hands]) == count_cards)
            summ += Card.score(Card(c), count_cards, leader)
        return summ

    def save(self):
        return ' '.join(map(str, self.cards))

    @classmethod
    def load(cls, text):
        cards = [Card.load(card) for card in text.split()]
        return Hand(cards)
