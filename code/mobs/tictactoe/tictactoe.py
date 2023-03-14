class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token



class Game():
    #init board
    def __init__(self) -> None:
        #defaults and make board
        #      cols:  0    1     2
        self.row1 = [' ', ' ',  ' ']
        self.row2 = [' ', ' ',  ' '] 
        self.row3 = [' ', ' ',  ' '] 
    #__str__ 
    def __str__(self) -> str: #assemble board
        for _ in self.row1:
            row1_print = '|'.join(self.row1)
        for _ in self.row2:
            row2_print = '|'.join(self.row2)
        for _ in self.row3:
            row3_print = '|'.join(self.row3)
        return(f'''
{row1_print}
{row2_print}
{row3_print}''')
    #move(x y player)
    def move(self, row, col, player):
        #row = '1' , '2', Player X
        row = int(row)
        col = int(col)


        if row == 0:
            row = self.row1
        elif row == 1:
            row = self.row2
        elif row == 2:
            row = self.row3

        if row[col] == ' ':
                row[col] = player.token
        else:
            print('Spot taken!')
            self.row = int(input('Row: '))
            self.col = int(input('Col: '))


        return self.__str__
    
    #calc_winner
    def calc_winner(self):
        row_win = 0
        rows = [self.row1, self.row2, self.row3]
        for row in rows:
            row_win = row.count('X')
            if row_win == 3:
                print('Condition met: horizontal win') #for horizontal wins only
        for i in range(len(rows)):
            if self.row1[i] == self.row2[i] == self.row3[i] and self.row1[i] != ' ':
                
                print('Condition met: vertical win')


        return #f'{self.player} is the winner!'
    
    #is_full
    def is_full(self):
        print('The board is full.')
        return self.is_game_over
    #is_game_over
    def is_game_over(self):
        return 'done'




#REPL for play
if __name__ == '__main__':
    token = ['X', 'O']
    #for symbol in token:
    playername1 = input('Enter X player name: ')
    playername2 = input('Enter O player name: ')
    playerX = Player(playername1, token[0])
    playerO = Player(playername2, token[1])

    players = [playerX, playerO]

    game = Game()
    print(game)

    while True:
        
        while True:
            print(f'{playername1}\'s turn!')
            row = input('Row: ')
            col = input('Col: ')
            game.move(row, col, playerX)
            print(game)
            break

        while True:
            print(f'{playername2}\'s turn!')
            row = input('Row: ')
            col = input('Col: ')
            game.move(row, col, playerO)
            print(game)
            break

        game.calc_winner()