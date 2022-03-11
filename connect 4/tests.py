import unittest

from board.board import Cell, Board
from game.game import Game
from players.computer import Computer
from players.human import Human

class TestBoard(unittest.TestCase):
    def test_board(self):
        board = Board(6, 7)
        assert board._lines == 6
        assert board._columns == 7
    def test_create_board(self):
        board = Board(6, 7)
        assert board._cells == board.create_board()
    def test_set_value(self):
        board = Board(6,7)
        board.set_value(2,3,"X")
        assert board._cells[2][3].value == "X"
    def test_return_empty_line(self):
        board = Board(6,7)
        assert board.return_empty_line(0) == 5
        for i in range(6):
            for j in range(7):
                board.set_value(i,j,"R")
        assert board.return_empty_line(0) == None
    def test_is_board_full(self):
        board = Board(6, 7)
        for i in range(6):
            for j in range(7):
                board.set_value(i, j, "R")
        assert board.is_board_full() == True
    def test_first_empty_cell(self):
        board = Board(6, 7)
        cell = board.return_first_empty_cell()
        assert cell.value == 0
        assert cell.line == 5
        assert cell.column == 0
        board.set_value(5,0,"R")
        cell = board.return_first_empty_cell()
        assert cell.value == 0
        assert cell.line == 5
        assert cell.column == 1
    def test_find_diagonal(self):
        board = Board(6, 7)
        assert board.find_diagonal(5) == (5,0)
        assert board.find_diagonal(7) == (5, 2)
    def test_second_diagonal(self):
        board = Board(6,7)
        assert board.find_second_diagonal(-1) == (5,6)
        assert board.find_second_diagonal(-4) == (2,6)
    def test_is_won(self):
        board = Board(6,7)
        board.set_value(5, 0, "R")
        board.set_value(4, 0, "R")
        board.set_value(3, 0, "R")
        board.set_value(2, 0, "R")
        assert board.is_won(Cell(0,2,"R")) == True

class TestHuman(unittest.TestCase):
    def test_move(self):
        board = Board(6,7)
        human = Human("R",board)
        human.move(0)
        assert board._cells[5][0].value == "R"

class TestComputer(unittest.TestCase):
    def test_computer(self):
        board = Board(6,7)
        computer = Computer("B", board)
        last_2_moves = [Cell(0,5,"R"),Cell(1,5,"B")]
        ok, cell = computer.move(last_2_moves)
        assert ok==False
        assert cell == Cell(0,5,"B")
        for i in range(3):
            board.set_value(5,i,"R")
        last_2_moves = [Cell(2, 5, "R"), Cell(1, 5, "B")]
        ok, cell = computer.move(last_2_moves)
        assert ok == False
        assert cell == Cell(3,5,"B")
        board._cells = board.create_board()
        board.set_value(5,0,"R")
        board.set_value(4, 0, "R")
        board.set_value(3, 0, "R")
        last_2_moves = [Cell(0,3,"R"), Cell(1,5,"B")]
        ok, cell = computer.move(last_2_moves)
        assert ok == False
        assert cell == Cell(0,2,"B")

class TestGame(unittest.TestCase):
    def test_game(self):
        board = Board(6, 7)
        computer = Computer("B", board)
        human = Human("R", board)
        game = Game(board,human,computer)
        assert type(game._player1) == Human
        assert type(game._player2) == Computer
if __name__ == '__main__':
    unittest.main()