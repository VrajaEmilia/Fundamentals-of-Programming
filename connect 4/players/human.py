from board.board import Cell


class Human:
    def __init__(self, value, board):
        self._value = value
        self._board = board

    def move(self,column):
        """
        takes user input and sets the value for the move in the board
        :param column: int
        :return: cell
        """
        line = self._board.return_empty_line(column)
        self._board.set_value(line, column, self._value)
        return Cell(column, line, self._value)
