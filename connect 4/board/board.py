from dataclasses import dataclass

class Board:
    def __init__(self, lines, columns, empty_value=0):
        self._lines = lines
        self._columns = columns
        self.__empty_value = empty_value
        self._cells = self.create_board()


    def create_board(self):
        """
        returns a self._lines x self._column matrix of empty Cells (Cell(0,0,0))
        :return: matrix
        """
        return [[Cell(line, column, self.__empty_value) for column in range(self._columns)]
                for line in range(self._lines)]

    def set_value(self, line, column, value):
        """
        places value in the board on the position given by the given column, lin
        :param line: int
        :param column: int
        :param value: any
        :return:
        """
        self._cells[line][column].value = value

    def __str__(self):
        res = ""
        for line in self._cells:
            s = "  ".join([str(cell.value) for cell in line]) + "\n"
            res += s
        return res

    def return_empty_line(self, column):
        """
        parses every line from the matrix and returns the first one where the given column is empty
        :param column: int
        :return: int
        """
        i = self._lines - 1
        while i>=0:
            if self._cells[i][column].value == 0:
                return i
            i-=1
        return None

    def is_board_full(self):
        """
        searches through the matrix for a cell with an empty value, it returns False if it finds one, True if it doesn't
        :return: bool
        """
        for cell in self.__get_all_cells_as_list():
            if cell.value == 0:
                return False
        return True

    def __get_all_cells_as_list(self):
        """
        returns the board as a list
        :return: list
        """
        return [cell for line in self._cells for cell in line]

    def is_won(self, last_move):
        """
        This method checks if the last move places on the board is a winning one
        returns True if it is, False if it's not
        :param last_move:  cell type object
        :return: bool
        """
        #horizontal
        k = 0
        horizontal = self.horizontal_win(last_move)
        vertical = self.vertical_win(last_move)
        diagonal = self.diagonal_win(last_move)
        other_diagonal = self.other_diagonal_win(last_move)
        if vertical == True or horizontal == True or diagonal == True or other_diagonal == True:
            return True
        return False

    def horizontal_win(self, last_move):
        """
        Takes the last move's line, and checks if there are 4 consecutive cells with the same value. If there are then the
        game is won and the method returns True, else returns False
        :param last_move:  cell type object
        :return: bool
        """
        k = 0
        for j in range(self._columns):
            if self._cells[last_move.line][j].value == last_move.value:
                k = k + 1
                if k == 4:
                    return True
            if self._cells[last_move.line][j].value != last_move.value:
                k = 0
        return False

    def vertical_win(self, last_move):
        """
        Takes the last move's column, and checks if there are 4 consecutive cells with the same value on that column.
        If there are then the game is won and the method returns True, else returns False
        :param last_move:  cell type object
        :return: bool
        """
        k = 0
        for i in range(self._lines):
            if self._cells[i][last_move.column].value == last_move.value:
                k = k + 1
                if k == 4:
                    return True
            if self._cells[i][last_move.column].value != last_move.value:
                k = 0
        return False

    def diagonal_win(self, last_move):
        """
         It goes through the matrix and when it finds the line and column for which line + column = last_move.line+last_move.column
        Checks if there are 4 consecutive cells with the same value on that diagonal. If there are then the game is won
        and the method returns True, else returns False
        :param last_move: cell type object
        :return: bool
        """
        k = 0
        for i in range(self._lines):
            for j in range(self._columns):
                if i + j == last_move.line + last_move.column and self._cells[i][j].value == last_move.value:
                    k +=1
                    if k == 4:
                        return True
                elif i + j == last_move.line + last_move.column and self._cells[i][j].value != last_move.value:
                    k = 0
        return False

    def other_diagonal_win(self, last_move):
        """
        It goes through the matrix and when it finds the line and column for which line - column = last_move.line-last_move.column
        Checks if there are 4 consecutive cells with the same value on that diagonal. If there are then the game is won
        and the method returns True, else returns False
        :param last_move: cell type object
        :return: bool
        """
        k = 0
        for j in range(self._columns):
            for i in range(self._lines):
                if i - j == last_move.line - last_move.column and self._cells[i][j].value == last_move.value:
                    k += 1
                    if k == 4:
                        return True
                elif i - j == last_move.line - last_move.column and self._cells[i][j].value != last_move.value:
                    k = 0
        return False


    def return_first_empty_cell(self):
        """
        It goes through the matrix from the last line, first column. Returns the first cell with the value 0
        :return: cell type object
        """
        line = self._lines - 1
        while line >= 0:
            for c in range(self._columns):
                if self._cells[line][c].value == 0:
                    return Cell(c, line, 0)
            line -= 1

    def find_diagonal(self, sum):
        """
         It goes through the matrix starting from the last line, first column. When line+column = sum then it has found the
         diagonal that has that sum and it returns the line and the column
        :param sum: int
        :return: int,int
        """
        column = 0
        line = self._lines - 1
        while line >= 0:
            if column + line == sum:
                return line,column
            if column == 6:
                column = -1
                line -= 1
            column += 1

    def find_second_diagonal(self, sub):
        """
        It goes through the matrix starting from the last line, first column. When line-column = sub then it has found the
        diagonal that has that sum and it returns the line and the column
        :param sum: int
        :return: int,int
        """
        column = 0
        line = self._lines - 1
        while line >= 0:
            if line-column == sub:
                return line, column
            if column == 6:
                column = -1
                line -= 1
            column += 1

@dataclass
class Cell:
    column: int
    line: int
    value: any


