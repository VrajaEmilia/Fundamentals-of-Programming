from board.board import Cell
from players.computer import Computer
from players.human import Human

class GameException(Exception):
    pass


class Game:
    def __init__(self, board, player1, player2):
        self._board = board
        self._player1 = player1
        self._player2 = player2

    def draw_board(self):
        print(self._board)

    def play_game(self):
        moves = 0
        last_move = Cell(0,0,0)
        last_2_moves = [Cell(0,0,0), Cell(0,0,0)]
        while self._board.is_board_full() == False:
            if moves > 0 and self._board.is_won(last_move) == True:
                self.draw_board()
                print("Game won by",last_move.value)
                break
            elif moves % 2 == 0:
                last_move = self._move(self._player1, last_2_moves)
                moves += 1
                last_2_moves[0] = last_move
            else:
                ok, last_move = self._move(self._player2,last_2_moves)
                last_2_moves[1] = last_move
                if ok == True:
                    self.draw_board()
                    print("Game won by", last_move.value)
                    break
                moves += 1
        print("GAME OVER")

    def _move(self, player, last_2_moves):
        if type(player) == Human:
            self.draw_board()
            column = self.read_input()
            last_move = self._player1.move(column)
            return last_move
        if type(player) == Computer:
            ok, last_move = self._player2.move(last_2_moves)
            return ok, last_move

    def read_input(self):
        data = False
        column = 0
        while data == False:
            column = input("Enter the column: ")
            data = self.check_column(column)
        return int(column)-1

    def check_column(self, column):
        if not column.isnumeric() or 1>int(column) or int(column) > 7:
            print("The column must be a number between 1 and 7")
            return False
        if self._board.return_empty_line(int(column)-1) == None:
            print("Column already full")
            return False
        return True