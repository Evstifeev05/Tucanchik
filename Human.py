from Player import Player


class Human(Player):
    def choose_row(self, rows, players):
        row = 0
        while row < 1 or row > 3 or not rows[row - 1].cards:
            row = input(f'Игрок "{self.name}" выберите стопку от 1 до 3 - ')
            try:
                row = int(row)
            except Exception:
                row = 0
        row = row - 1
        self.hand.add_cards(rows[row].take_cards())
        return row
