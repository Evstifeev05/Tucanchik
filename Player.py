from Hand import Hand


class Player:
    def __init__(self, name, hand=None):
        self.name = name
        if hand is None:
            hand = Hand()
        self.hand = hand

    def __str__(self):
        return f'{self.name}'

    def choose_row(self, rows, players):
        pass

    def save(self):
        return {'name': self.name,
                'hand': self.hand.save()}
