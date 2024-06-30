import unittest

from Hand import Hand


class HandTest(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()

    def test_add_cards(self):
        cards = ['banana', 'fig', 'avocado']
        self.hand.add_cards(cards)
        self.assertEqual(self.hand.cards, cards)


if __name__ == '__main__':
    unittest.main()
