from Card import Card


def test_score():
    card = Card('acai')
    assert Card.score(card, 4) == 5
