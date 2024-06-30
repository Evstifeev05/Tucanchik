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

    def score(self):
        summ = 0
        set_cards = set(self.cards)
        for card in set_cards:
            count_cards = self.cards.count(card)
            summ += Card.score(card, count_cards)
        return summ

    def save(self):
        return ' '.join(map(str, self.cards))
