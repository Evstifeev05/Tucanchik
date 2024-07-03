import random
from Card import Card


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
            for key in Card.CARD_COUNTS:
                for i in range(Card.CARD_COUNTS[key]):
                    cards.append(Card(key))
        self.cards = cards

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        return None

    def shuffle(self):
        random.shuffle(self.cards)

    def remaining_cards(self):
        return len(self.cards)

    def save(self):
        return ' '.join(map(str, self.cards))

    @classmethod
    def load(cls, text):
        cards = [Card.load(card) for card in text.split()]
        return Deck(cards)
