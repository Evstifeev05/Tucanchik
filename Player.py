import random

from Hand import Hand


class Player:
    def __init__(self, name, hand=None, is_human=False):
        self.name = name
        if hand is None:
            hand = Hand()
        self.hand = hand
        if is_human:
            self.actor = Human()
        else:
            self.actor = AI()

    def __str__(self):
        return f'{self.name}'

    def choose_row(self, rows, players):
        return self.actor.choose_row(self, rows)

    def save(self):
        return {'name': self.name,
                'hand': self.hand.save(),
                'is_human': isinstance(self.actor, Human)}

    @classmethod
    def load(cls, data: dict):
        name = data['name']
        hand = Hand.load(data['hand'])
        is_human = data['is_human']
        return Player(name, hand, is_human)


class Human:
    @staticmethod
    def choose_row(player, rows):
        row = 0
        while row < 1 or row > 3 or not rows[row - 1].cards:
            row = input(f'Игрок "{player.name}" выберите стопку от 1 до 3 - ')
            try:
                row = int(row)
            except Exception:
                row = 0
        row = row - 1
        player.hand.add_cards(rows[row].take_cards())
        return row


class AI:
    @staticmethod
    def choose_row(player, rows):
        row = random.randint(0, 2)
        print(f'"{player.name}" выбрал {row + 1} стопку')
        player.hand.add_cards(rows[row].take_cards())
        return row
