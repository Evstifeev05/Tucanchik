from GameState import GameState
from Human import Human


class GameInteractions:

    @staticmethod
    def run():
        count_players = GameInteractions.input_count_players(2, 4)
        humans = GameInteractions.input_human_names(count_players)
        game_state = GameState(humans)
        while game_state.deck.remaining_cards() > len(game_state.players):
            for _ in range(count_players):
                GameInteractions.print_rows(game_state.rows)

                current_player = game_state.players[game_state.current_player]

                game_state.take_row(game_state.current_player,
                                    current_player.choose_row(game_state.rows, game_state.players))
                game_state.save()
            print('-----------')
        GameInteractions.print_results(game_state)

    @staticmethod
    def input_count_players(minim, maxim):
        count = minim - 1
        while count < minim or count > maxim:
            count = input(f'Введите кол-во игроков от {minim} до {maxim} - ')
            try:
                count = int(count)
            except Exception:
                count = minim - 1
        return count

    @staticmethod
    def input_human_names(count):
        humans = []
        for i in range(count):
            name = input(f'[{i + 1}] Введите имя игрока - ')
            humans.append(Human(name))
        return humans

    @staticmethod
    def print_rows(rows):
        print(f'Стопки:')
        for i in range(3):
            print(f'{i + 1}-я cтопка: {rows[i]}')

    @staticmethod
    def print_results(game_state):
        print('Очки:')
        maxim = 0
        for player in game_state.players:
            print(f'{player} - {player.hand.score()}')
            if player.hand.score() > maxim:
                maxim = player.hand.score()
                winner = player
        print('**************************')
        print(f'{winner} ({maxim} очков) - ПОБЕДИТЕЛЬ!')
        print('**************************')
