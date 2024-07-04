import unittest

from Card import Card
from Hand import Hand


class HandTest(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def test_add_cards(self):
        cards = [Card('banana'), Card('fig'), Card('avocado')]
        self.hand.add_cards(cards)
        self.assertEqual(self.hand.cards, cards)

    def test_score(self):
        cards = [Card('acai'), Card('fig'), Card('fig'), Card('fig')]
        self.hand.add_cards(cards)
        self.assertEqual(self.hand.score(), 10)


if __name__ == '__main__':
    unittest.main()
