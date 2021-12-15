class Board:
    '''Draws the board '''

    def __init__(self, g1='g1', g2='g2', g3='g3', g4='g4', g5='g5', g6='g6', g7='g7', g8='g8', g9='g9'):
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
        self.g4 = g4
        self.g5 = g5
        self.g6 = g6
        self.g7 = g7
        self.g8 = g8
        self.g9 = g9

        self.draw()

    def draw(self):

        print(f'\t{self.g1}\t|\t {self.g2}\t|\t {self.g3}\t|')
        print(f'\t___\t|\t___\t|\t___\t|')
        print(f'\t{self.g4}\t|\t{self.g5}\t|\t{self.g6}\t|')
        print(f'\t___\t|\t___|\t___\t|')
        print(f'\t{self.g7}\t|\t {self.g8}\t|\t{self.g9}\t|')

    def mark_board(self, chosen_grid, player):

        if chosen_grid == 'g1' and self.g1.__contains__('g1'):
            self.g1 = player
            self.draw()
        elif chosen_grid == 'g2' and self.g2.__contains__('g2'):
            self.g2 = player
            self.draw()
        elif chosen_grid == 'g3' and self.g3.__contains__('g3'):
            self.g3 = player
            self.draw()
        elif chosen_grid == 'g4' and self.g4.__contains__('g4'):
            self.g4 = player
            self.draw()
        elif chosen_grid == 'g5' and self.g5.__contains__('g5'):
            self.g5 = player
            self.draw()
        elif chosen_grid == 'g6' and self.g6.__contains__('g6'):
            self.g6 = player
            self.draw()
        elif chosen_grid == 'g7' and self.g7.__contains__('g7'):
            self.g7 = player
            self.draw()
        elif chosen_grid == 'g8' and self.g8.__contains__('g8'):
            self.g8 = player
            self.draw()
        elif chosen_grid == 'g9' and self.g9.__contains__('g9'):
            self.g9 = player
            self.draw()

    # check for win
    def game_over(self):

        # check for horizontal line
        if (self.g1 == self.g2 == self.g3) :
            print("Game Over horzontal win")
            return True
        if (self.g4 == self.g5 == self.g6):
            print("Game Over  horzontal win")
            return True
        if (self.g7 == self.g8 == self.g9) :
            print("Game Over  horzontal win")
            return True
        # check for vertical line
        if (self.g1 == self.g4 == self.g7) :
            print("Game Over vertical win")
            return True
        if (self.g2 == self.g5 == self.g8):
            print("Game Over  vertical win")
            return True
        if (self.g3 == self.g6 == self.g9):
            print("Game Over  vertical win")
            return True
        # check diagonal
        if (self.g1 == self.g5 == self.g9) :
            print("Game Over  diagonal win ")
            return True
        if (self.g7 == self.g5 == self.g3):
            print("Game Over  diagonal win")
            return True
        return False
