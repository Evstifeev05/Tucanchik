class Row:
    def __init__(self, cards: list):
        self.cards = cards
        if cards is None:
            self.cards = []

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def add_card(self, card):
        if card is not None:
            self.cards.append(card)

    def take_cards(self):
        cards = self.cards.copy()
        self.cards.clear()
        return cards

    def save(self):
        return ' '.join(map(str, self.cards))
