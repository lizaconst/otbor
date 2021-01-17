from random import randint, sample
import copy

class Board:
    def __init__(self, cells):
        self.cells = cells
        self.game_board =           [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                     [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                     [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                     [2, 3, 4, 5, 6, 7, 8, 9, 1],
                                     [5, 6, 7, 8, 9, 1, 2, 3, 4],
                                     [8, 9, 1, 2, 3, 4, 5, 6, 7],
                                     [3, 4, 5, 6, 7, 8, 9, 1, 2],
                                     [6, 7, 8, 9, 1, 2, 3, 4, 5],
                                     [9, 1, 2, 3, 4, 5, 6, 7, 8]]
        self.game_board_delete = None
    
    def transpose(self):
        new = copy.deepcopy(self.game_board)
        for i in range(9):
            for j in range(9):
                new[j][i] = self.game_board[i][j]
        self.game_board = copy.deepcopy(new)
                
    def change_rows(self):
        n = randint(0, 2)
        r_1 = randint(0, 2)
        r_2 = randint(0, 2)
        row_1 = n*3 + r_1
        row_2 = n*3 + r_2 
        a = self.game_board
        a[row_1], a[row_2] = a[row_2], a[row_1]
        
    def change_cols(self):
        self.transpose()
        self.change_rows()
        self.transpose()
        
    def change_areas_rows(self):
        n_1 = randint(0, 2)*3
        n_2 = randint(0, 2)*3
        a = self.game_board
        a[n_1:n_1+3],  a[n_2:n_2+3] = a[n_2:n_2+3],  a[n_1:n_1+3]
    
    def change_areas_cols(self):
        self.transpose()
        self.change_areas_rows()
        self.transpose()
        
    def delete_cells(self):
        self.game_board_delete = copy.deepcopy(self.game_board)
        rows = sample([w for w in range(0, 81)], k = self.cells)
        for i in range(self.cells):
            self.game_board_delete[rows[i] // 9][rows[i] % 9] = 0    
    
    def create_board(self):
        i = randint(50, 100)
        for j in range(i):
            k = randint(0, 4)
            if k == 0:
                self.transpose()
            if k == 1:
                self.change_rows()
            if k == 2:
                self.change_cols()
            if k == 3:
                self.change_areas_rows()
            if k == 4:
                self.change_areas_cols()
        self.delete_cells()
                
    def show_board(self):
        for i in range(9):
            print(self.game_board[i])
                
    def show_board_deleted(self):
        for i in range(9):
            print(self.game_board_delete[i])

class Game:
    def __init__(self, cells):
        self.cells = 81 - cells
        self.board = Board(self.cells)
        self.board.create_board()
    
    def show_for_user(self):
        for i in range(9):
            if i == 3 or i == 6:
                print('\n')
            for j in range(9):
                if j == 3 or j == 6:
                    print('     ', end='')
                print(self.board.game_board_delete[i][j], end=' ') 
            print('\n')
            
    def show_full_board(self):
        for i in range(9):
            if i == 3 or i == 6:
                print('\n')
            for j in range(9):
                if j == 3 or j == 6:
                    print('     ', end='')
                print(self.board.game_board[i][j], end=' ') 
            print('\n')

#пример доски
print('\nпример доски\n')
game = Game(50)
game.show_for_user()
#пример сгенерированной доски
print('\nпример сгенерированной доски\n')
game = Game(50)
game.show_full_board()
