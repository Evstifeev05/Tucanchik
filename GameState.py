import json

from Deck import Deck
from Row import Row


class GameState:
    def __init__(self, players, current_player=0, deck=None, rows=None):
        if deck is None:
            deck = Deck()
            deck.shuffle()

        if rows is None:
            self.put_rows(deck)
        else:
            self.rows = rows

        self.players = players
        self.current_player = current_player
        self.deck = deck

    def add_cards(self):
        for i in range(len(self.rows)):
            self.rows[i].add_card(self.deck.draw_card())

    def take_row(self, player, row):
        self.players[player].hand.add_cards(self.rows[row].take_cards())
        self.current_player = (self.current_player + 1) % len(self.players)
        self.add_cards()

    def put_rows(self, deck):
        self.rows = [Row([deck.draw_card()]),
                     Row([deck.draw_card(), deck.draw_card()]),
                     Row([deck.draw_card()])]

    def save(self):
        with open('save.json', 'w', encoding='utf-8') as f:
            json.dump({'players': [player.save() for player in self.players],
                       'current_player': self.current_player,
                       'rows': [row.save() for row in self.rows],
                       'deck': self.deck.save()}, f, indent=4)
