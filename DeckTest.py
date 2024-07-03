from Card import Card
from Deck import Deck


def test_draw_card():
    deck = Deck([Card('acai'), Card('fig'), Card('fig'), Card('fig')])
    card = deck.draw_card()
    assert str(card) == str(Card('fig'))
    assert str(deck) == str(Deck([Card('acai'), Card('fig'), Card('fig')]))


def test_remaining_cards():
    deck = Deck([Card('acai'), Card('fig'), Card('fig'), Card('fig')])
    assert deck.remaining_cards() == 4


test_draw_card()
test_remaining_cards()
