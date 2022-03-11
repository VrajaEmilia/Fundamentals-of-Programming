
from board.board import Board
from game.game import Game
from players.computer import Computer
from players.human import Human

if __name__ == '__main__':
    board = Board(6,7)
    player1 = Human("R", board)
    #strategy = NoStrategy()
    player2 = Computer("B", board)
    game = Game(board, player1, player2)
    game.play_game()