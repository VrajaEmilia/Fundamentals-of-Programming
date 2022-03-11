from board.board import Cell


class Computer:
    def __init__(self, value, board):
        self._value = value
        self._board = board

    def move(self, last_2_moves):
        """
        Checks if the next move can be a winning one. If true moves in that cell. If False, it checks if the other player is
        one move away from winning, if it is it blocks them. Else it moves in the first empty cell found
        :param last_2_moves: cell type object
        :return: bool, cell type object
        """
        ok, cell = self.check_winning_move(self._value, last_2_moves[1])
        if ok:
            self._board.set_value(cell.line, cell.column, self._value)
            return ok, cell

        ok, i ,j = self.block_winning_move(last_2_moves[0].value,last_2_moves[0])
        if ok:
            self._board.set_value(i,j,self._value)
            ok = False
            return ok, Cell(j, i, self._value)

        cell = self._board.return_first_empty_cell()
        self._board.set_value(cell.line, cell.column, self._value)
        return ok, Cell(cell.column, cell.line, self._value)

    def check_winning_move(self, value, last_move):
        """
        Calls all the methods to check if the next move can be a winning one. When ok is true it means that the computer
        can make the final move and it returns the cell.
        Else it returns False, meaning that the game can't be won, and an empty cell
        :param value: any
        :param last_move: cell type object
        :return: bool, cell type object
        """
        ok, i, j = self.check_if_3_vertical(value)
        if ok:
            return ok, Cell(j,i,value)

        ok, i, j = self.check_if_3_diagonally(value, last_move)
        if ok:
            return ok, Cell(j,i,value)

        ok, i, j = self.check_if_3_horizontally(value, last_move)
        if ok:
            return ok, Cell(j,i,value)

        ok, i, j = self.check_if_3_second_diagonal(value, last_move)
        if ok:
            return ok, Cell(j, i, value)

        return False, Cell(0,0,0)

    def check_if_3_vertical(self, value):
        """
        Goes through every column and check if there are 3 consecutive cells that have the given value
        Returns True and the Cell.line, cell.column in which the computer needs to move either to block
        the other player, or to win
        Or False if there aren't 3 consecutive cells with the same value
        :param value: any
        :return:bool, int, int
        """
        column = 0
        while column <= self._board._columns - 1:
            k = 0
            i = self._board._lines - 1
            while i >= 0:
                if self._board._cells[i][column].value == value:
                    k +=1
                    if k == 3 and i > 0 and self._board._cells[i - 1][column].value == 0:
                        return True, i-1, column
                elif self._board._cells[i][column].value != value:
                    k = 0
                i -= 1
            column += 1
        return False, 0, 0

    def check_if_3_diagonally(self, value, last_move):
        """
        goes through the diagonal that has last_move.line+last_move.column = line + column. if there are 3 consecutive
        cells that have the given value. Returns True and the Cell.line, cell.column in which the computer needs to move either to block
        the other player, or to win
        Or False if there aren't 3 consecutive cells with the same value on that diagonal
        :param value: any
        :param last_move: cell type object
        :return: bool, int, int
        """
        k = 0
        line, column = self._board.find_diagonal(last_move.line+last_move.column)
        while line > 0 and column < 6:
            if self._board._cells[line][column].value == value:
                k +=1
                if k == 3 and self._board._cells[line-1][column+1].value == 0 and self._board._cells[line][column+1].value != 0:
                    return True, line-1, column+1
            if self._board._cells[line][column].value != value:
                k = 0
            line -= 1
            column += 1
        return False, 0, 0

    def check_if_3_second_diagonal(self, value, last_move):
        """
            goes through the diagonal that has last_move.line-last_move.column = line - column. if there are 3 consecutive
            cells that have the given value. Returns True and the Cell.line, cell.column in which the computer needs to move either to block
            the other player, or to win
            Or False if there aren't 3 consecutive cells with the same value on that diagonal
            :param value: any
            :param last_move: cell type object
            :return: bool, int, int
            """
        k = 0
        line, column = self._board.find_second_diagonal(last_move.line - last_move.column)
        while line > 0 and column > 0:
            if self._board._cells[line][column].value == value:
                k += 1
                if k == 3 and self._board._cells[line-1][column-1].value == 0 and self._board._cells[line][column-1].value != 0:
                    return True, line-1, column-1
            if self._board._cells[line][column].value != value:
                k = 0
            line -= 1
            column -= 1
        return False, 0,0

    def check_if_3_horizontally(self, value, last_move):
        """
        Goes through every line and checks if there are 3 consecutive cells that have the given value
        Returns True and the Cell.line, cell.column in which the computer needs to move either to block
        the other player, or to win
        Or False, 0, 0 if there aren't 3 consecutive cells with the same value
        :param value: any
        :return:bool, int, int
        """
        k = 0
        line = last_move.line
        column = 0
        while column <= 6:
            if self._board._cells[line][column].value == value:
                k += 1
                if k == 3 and column < 6 and self._board._cells[line][column+1].value == 0:
                    if line < self._board._lines - 1 and self._board._cells[line+1][column+1].value !=0:
                        return True, line, column + 1
                    if line == self._board._lines - 1:
                        return True, line, column + 1
                if k == 3 and column > 3 and self._board._cells[line][column-3].value == 0:
                    if line <  self._board._lines - 1 and self._board._cells[line + 1][column - 3].value != 0:
                        return True, line, column - 3
                    if line == self._board._lines - 1:
                        return True, line, column - 3
            if self._board._cells[line][column].value != value:
                k = 0
            column +=1
        return False, 0 ,0

    def block_winning_move(self, value, last_move):
        """
        Calls all the method to check if the opponent has 3 consecutive pieces horizontally, vertically or diagonally
        Returns True if it finds them and the line and column for the cell in which the computer needs to move
        to block the player
        :param value: any
        :param last_move: cell type object
        :return: bool, int, int
        """
        if value != 0:
            ok,i,j = self.check_if_3_vertical(value)
            if ok == True :
                return ok, i, j
            ok, i, j = self.check_if_3_diagonally(value, last_move)
            if ok == True :
                return ok, i, j
            ok, i ,j = self.check_if_3_horizontally(value, last_move)
            if ok == True :
                return ok, i, j
            ok, i, j = self.check_if_3_second_diagonal(value, last_move)
            if ok == True:
                return ok, i, j
        return False, 0, 0
