class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game():
    # init board
    def __init__(self) -> None:
        # defaults and make board
        #      cols:  0    1     2
        self.row1 = [' ', ' ',  ' ']
        self.row2 = [' ', ' ',  ' ']
        self.row3 = [' ', ' ',  ' ']
        # self.row1 = [' ', 'O',  'X']
        # self.row2 = ['X', 'O',  'X']
        # self.row3 = ['X', 'O',  'X']

    def __str__(self) -> str:  # assemble board
        for _ in self.row1:
            row1_print = '|'.join(self.row1)
        for _ in self.row2:
            row2_print = '|'.join(self.row2)
        for _ in self.row3:
            row3_print = '|'.join(self.row3)
        return (f'''
{row1_print}
{row2_print}
{row3_print}''')

    def move(self, row, col, player):
        # row = '1' , '2', Player X
        row = int(row)
        col = int(col)

        if row == 0:
            board_row = self.row1
        elif row == 1:
            board_row = self.row2
        elif row == 2:
            board_row = self.row3
        else:
            return False

        if board_row[col] == ' ':
            board_row[col] = player.token
        else:
            print('Spot taken!')
            return False

        return self.__str__

    # calc_winner
    def calc_winner(self, player):
        row_win = 0
        rows = [self.row1, self.row2, self.row3]
        for row in rows:
            row_win = row.count(player.token)
            if row_win == 3:
                # for horizontal wins only
                print('Condition met: horizontal win')
                return player
        for i in range(len(rows)):
            if self.row1[i] == self.row2[i] == self.row3[i] and self.row1[i] != ' ':
                print('Condition met: vertical win')
                return player
        if self.row1[0] == self.row2[1] == self.row3[2] and self.row1[0] != ' ':
            print('diagonal win')
            return player
        if self.row1[2] == self.row2[1] == self.row3[0] and self.row1[2] != ' ':
            print('diagonal win')
            return player

        return None

    def is_full(self):
        if self.row1.count(' ') != 0:
            return False
        if self.row2.count(' ') != 0:
            return False
        if self.row3.count(' ') != 0:
            return False
        print('The board is full.')
        return True

    def is_game_over(self, players):
        has_winner = self.calc_winner(
            players[0]) is not None and self.calc_winner(players[1]) is not None
        if self.is_full() or has_winner:
            return True
        return False


# encapsulate logic into helper functions!
def play_round(game: Game, player: Player):
    valid_choices = ['0', '1', '2']

    print(f'{player.name}\'s turn!')
    row = input('Row: ')
    col = input('Col: ')

    if row in valid_choices and col in valid_choices:
        move_allowed = game.move(row, col, player)
    else:
        print("invalid input")
        play_round(game, player)

    if not move_allowed:
        play_round(game, player)

    print(game)
    return game.calc_winner(player)


# REPL for play
if __name__ == '__main__':
    token = ['X', 'O']
    # for symbol in token:
    playername1 = input('Enter X player name: ')
    playername2 = input('Enter O player name: ')
    playerX = Player(playername1, token[0])
    playerO = Player(playername2, token[1])

    players = [playerX, playerO]

    game = Game()
    print(game)

    winner = None
    while winner is None:
        winner = play_round(game, playerX)
        if game.is_game_over([playerX, playerO]):
            break
        if winner is None:
            winner = play_round(game, playerO)
            if game.is_game_over([playerX, playerO]):
                break
        if winner is not None:
            print(f'{winner.name} won the game')
            break
