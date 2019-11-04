
import numpy as np
import math

BLACK = 1
WHITE = 2
EMPTY = 0
BORDER = 3


class MC_Player(object):
    def __init__(self, color):
        self.name = "Chinese Checkers player"
        self.version = 1.0
        self.color = color
        self.N = 10
        self.max = 10
        self.best = 3  # randomize on best 1/self.best
        self.startmoves = {}
        #self.board = board

    # input: board is the current class that is the board and all its methods

    def play_move(self, board):
        # impliment a random player form the board
        moves = board.move_ordering(self.color)
        values = np.zeros(len(moves))
        for m in range(len(moves)):
            out = 0
            for s in range(self.N):
                out += self.simulate(board, moves[m], self.color)
            values[m] = (out*100)/self.N
        i = np.argmax(values)
        move = moves[i]
        if values[i] == 0.0:
            move = moves[np.random.randint(math.ceil(len(moves)/self.best))]
        board.play_move(move[0], move[1], self.color)

    def simulate(self, board, move, color):
        b_copy = board.copy()
        b_copy.play_move(move[0], move[1], color)
        c = 0
        curr = b_copy.opponent(color)
        while(c < self.max):
            c += 1
            term = b_copy.terminal()
            if term == color:
                return 1
            elif term == b_copy.opponent(color):
                return 0
            n_moves = b_copy.move_ordering(curr)
            n_move = n_moves[np.random.randint(
                math.ceil(len(n_moves)/self.best))]
            b_copy.play_move(n_move[0], n_move[1], curr)
            curr = b_copy.opponent(curr)
        return 0

    def did_win(self, winner):
        if winner == self.color:
            pass
        else:
            pass


class Random_Player(object):
    def __init__(self, color):
        self.name = "Chinese Checkers player"
        self.version = 1.0
        self.color = color
        #self.board = board

    # input: board is the current class that is the board and all its methods

    def play_move(self, board):
        # impliment a random player form the board
        moves = board.move_ordering(self.color)
        move = moves[np.random.randint(len(moves))]
        board.play_move(move[0], move[1], self.color)


class Ordered_Player(object):
    def __init__(self, color):
        self.name = "Chinese Checkers player"
        self.version = 1.0
        self.color = color
        #self.board = board

    # input: board is the current class that is the board and all its methods

    def play_move(self, board):
        # impliment a random player form the board
        moves = board.move_ordering(self.color)
        move = moves[np.random.randint(math.ceil(len(moves)/3))]
        board.play_move(moves[0][0], moves[0][1], self.color)
