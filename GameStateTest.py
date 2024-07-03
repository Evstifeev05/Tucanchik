from Card import Card
from GameState import GameState
from Player import Player
from Row import Row


def test_take_row():
    players = [Player('A'), Player('B')]
    rows = [Row([Card('acai'), Card('coconut'), Card('carambola')]), Row([Card('coconut')]), Row([Card('acai')])]
    game_state = GameState(players, 0, None, rows)

    row = rows[0].cards.copy()
    game_state.take_row(0, 0)
    assert str(players[0].hand.cards) == str(row)
