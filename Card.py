class Card:
    KINDS = ['acai', 'avocado', 'banana', 'carambola', 'coconut', 'fig', 'lime', 'lychee', 'orange', 'papaya',
             'pineapple', 'pomegranate', 'rambutan']
    CARD_COUNTS = {'acai': 6, 'avocado': 5, 'banana': 5, 'carambola': 5, 'coconut': 6, 'fig': 4, 'lime': 2, 'lychee': 2,
                   'orange': 4, 'papaya': 4, 'pineapple': 3, 'pomegranate': 6, 'rambutan': 5}
    CARD_BONUS = {'acai': (1, 2, 3, 5, 8, 13), 'carambola': (1, 3, 6, 10, 15), 'coconut': (8, 6, 4, 2, 0, -2),
                  'fig': (-2, 0, 9, 16), 'lime': (-2, -8), 'lychee': (5, 12), 'orange': (4, 8, 12, 0),
                  'papaya': (1, 1, 9, 20), 'pineapple': (0, -2, -4), 'rambutan': (3, 6, 9, 12, 15)}
    CARD_SPEC = {'avocado': (1, 3), 'banana': (0, 2), 'pomegranate': (-1, 1)}

    def __init__(self, kind):
        self.kind = kind

    def __str__(self):
        return self.kind

    @staticmethod
    def score(card, count, leader=False):
        if count == 0:
            return 0
        if card.kind in Card.CARD_SPEC:
            return Card.CARD_SPEC[card.kind][leader] * count
        return Card.CARD_BONUS[card.kind][count - 1]

    def save(self):
        return self.kind

    @classmethod
    def load(cls, text: str):
        return Card(text)
