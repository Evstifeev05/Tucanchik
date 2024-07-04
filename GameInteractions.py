from GameState import GameState
from Player import Player


class GameInteractions:

    @staticmethod
    def run():
        new_game = False
        try:
            game_state = GameState.load('save.json')
        except Exception:
            new_game = True

        continue_game = ''
        if not new_game:
            continue_game = input('Чтобы продолжить предыдущую игру введите "да" - ')

        if new_game or not continue_game == 'да':
            count_players = GameInteractions.input_count_players(2, 4)
            count_bots = GameInteractions.input_count_bots(count_players)
            humans = GameInteractions.input_human_names(count_players - count_bots)
            bots = GameInteractions.create_bots(count_bots)
            game_state = GameState(humans + bots)
        else:
            game_state = GameState.load('save.json')

        while game_state.deck.remaining_cards() > len(game_state.players):
            for _ in range(len(game_state.players)):
                GameInteractions.print_rows(game_state.rows)

                current_player = game_state.players[game_state.current_player]
                row = current_player.choose_row(game_state.rows, game_state.players)
                game_state.take_row(game_state.current_player, row)
                game_state.current_player = (game_state.current_player + 1) % len(game_state.players)
                game_state.add_cards()

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
    def input_count_bots(maxim):
        count = -1
        while count < 0 or count > maxim:
            count = input(f'Введите количество ботов (не больше {maxim}) - ')
            try:
                count = int(count)
            except Exception:
                count = -1
        return count

    @staticmethod
    def create_bots(count_bots):
        bots = []
        for i in range(count_bots):
            bots.append(Player(f'Bot {i + 1}', is_human=False))
        return bots

    @staticmethod
    def input_human_names(count):
        humans = []
        for i in range(count):
            name = input(f'[{i + 1}] Введите имя игрока - ')
            humans.append(Player(name, is_human=True))
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
        hands = [h.hand for h in game_state.players]
        for player in game_state.players:
            print(f'{player} - {player.hand.score(hands)}')
            if player.hand.score() > maxim:
                maxim = player.hand.score(hands)
                winner = player
        print('**************************')
        print(f'{winner} ({maxim} очков) - ПОБЕДИТЕЛЬ!')
        print('**************************')
