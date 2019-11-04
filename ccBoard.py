import numpy as np
from graphics import *
from random import *
from math import *
import time

BLACK = 1
WHITE = 2
EMPTY = 0
BORDER = 3


# FUNCTIONS
class ChineseCheckers(object):
    def __init__(self):
        # self.player = BLACK
        # self.board = np.array([3,3,3,3,3,1,1,0,3,1,0,2,3,0,2,2,3,3,3,3]) #3x3
        # self.term = np.array([3,3,3,3,3,2,2,0,3,2,0,1,3,0,1,1,3,3,3,3]) #3x3
        # self.values = np.array([[0,0,0,0,0,2,3,4,0,3,4,5,0,4,5,6,0,0,0,0],[0,0,0,0,0,6,5,4,0,5,4,3,0,4,3,2,0,0,0,0]])
        # self.path = []
        # self.board_size = 4 #3+1padding

        self.board = np.array([3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 0, 0, 3, 1, 1, 0, 0, 0,
                               3, 1, 0, 0, 0, 2, 3, 0, 0, 0, 2, 2, 3, 0, 0, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3])

        self.board_copy = np.array([3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 0, 0, 3, 1, 1, 0, 0, 0,
                                    3, 1, 0, 0, 0, 2, 3, 0, 0, 0, 2, 2, 3, 0, 0, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3])

        self.term = np.array([3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0, 0, 3, 2, 2, 0, 0, 0,
                              3, 2, 0, 0, 0, 1, 3, 0, 0, 0, 1, 1, 3, 0, 0, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3])

        self.values = np.array([[0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 5, 6, 0, 3, 4, 5, 6, 7, 0, 4, 5, 6, 7, 8, 0, 5, 6, 7, 8, 9, 0, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 10, 9, 8, 7, 6, 0, 9, 8, 7, 6, 5, 0, 8, 7, 6, 5, 4, 0, 7, 6, 5, 4, 3, 0, 6, 5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0]])

        self.path = []
        self.board_size = 6  # 5+1padding

        self.moves = []
        self.ttable = {}

        self.adj = [1, -1, self.board_size, -self.board_size,
                    self.board_size-1, -self.board_size+1]
        self.hop = [2, -2, 2*self.board_size, -2*self.board_size,
                    2*self.board_size-2, -2*self.board_size+2]


# ----------------------------------------------------------------------------------------------------------------------------------------------------


    def make_hexagon(self, x, y):
        h = Polygon([Point(x, y), Point(x, y+10), Point(x+10, y+20),
                     Point(x+20, y+10), Point(x+20, y), Point(x+10, y-10)])
        return h

    def print_graph_board(self):
        self.board_obj = []
        self.win = None
        self.win = GraphWin('Chinese Checkers', 150, 250)
        # resets the board and color lists when it is recalled when you go to the main menu

        start = [50, 40]

        for i in range(self.board_size - 1):
            for j in range(self.board_size - 1):
                h = self.make_hexagon(start[0] + j*10, start[1] + j*20)
                # h.setFill("orange")
                h.draw(self.win)
                self.board_obj.append(h)

            start[0] -= 10
            start[1] += 20

    def update_graph_board(self):
        for i in range(len(self.board)):
            if self.board[i] == BLACK:
                self.board_obj[self.index_convert(i)].setFill("purple4")
                # self.board_obj[self.index_convert(i)].draw(self.win)
                update()
            elif self.board[i] == WHITE:
                self.board_obj[self.index_convert(i)].setFill("lightblue")
                # self.board_obj[self.index_convert(i)].draw(self.win)
                update()
            elif self.board[i] == EMPTY:
                self.board_obj[self.index_convert(i)].setFill("white")
                # self.board_obj[self.index_convert(1)].draw(self.win)
                update()
            else:
                continue
        # self.win.getMouse()
        # time.sleep(0.08)

    def index_convert(self, index):
        return (((index//self.board_size)-1)*(self.board_size-1))+((index % self.board_size)-1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------

    def print_board(self):
        print_str = ''
        chars = [' .', ' b', ' w', '\n']
        for i in range(self.board_size, len(self.board)-self.board_size):
            print_str += chars[self.board[i]]
        # print_str += str(i)
        print(print_str)

    def opponent(self, p):
        if p == BLACK:
            return WHITE
        else:
            return BLACK
    '''
    def switch_player(self):
        self.player = self.opponent(self.player)
    '''

    def play_move(self, start, end, player):
        if (self.board[start] == player) and (self.board[end] == EMPTY):
            self.board[start] = EMPTY
            self.board[end] = player
        # self.switch_player()
        else:
            #print('error: unable to play move '+str(start)+' '+str(end))
            pass

    def remove_move(self, start, end, player):
        if (self.board[start] == EMPTY) and (self.board[end] == player):
            # self.switch_player()
            self.board[start] = player
            self.board[end] = EMPTY
        else:
            print('error: unable to remove move '+str(start)+' '+str(end))

    def find_moves(self, player):
        self.moves = []
        pieces = np.where(self.board == player)
        for piece in pieces[0]:
            for a in self.adj:
                if (self.board[piece+a] == EMPTY):
                    self.moves.append([piece, piece+a])
            self.hop_moves(piece, piece)
        # return self.moves
        # print(self.moves)

    def hop_moves(self, og, curr):
        for i in range(len(self.adj)):
            if (self.board[curr+self.adj[i]] == BLACK) or (self.board[curr+self.adj[i]] == WHITE):
                if (self.board[curr+self.hop[i]] == EMPTY) and not ([og, curr+self.hop[i]] in self.moves):
                    self.moves.append([og, curr+self.hop[i]])
                    self.hop_moves(og, curr+self.hop[i])

    def terminal(self):
        '''
    for p in range(1,3):
      b = (self.board == p)
      t = (self.term == p)
      if np.array_equal(b,t):
        return p
    return 0
    '''
        for p in range(1, 3):
            t = (self.term == p)
            v = [0, 0, 0]
            for b in range(len(self.board)):
                if t[b]:
                    v[self.board[b]] += 1
            if v[p] == np.sum(t):
                return p
            if (v[p] == np.sum(t)-1) and (v[self.opponent(p)] == 1):
                return p
        return 0

    def move_ordering(self, player):
        self.find_moves(player)
        valmoves = []
        for move in self.moves:
            self.play_move(move[0], move[1], player)
            binary = (self.board == player)
            valarr = np.multiply(binary, self.values[player-1])
            value = np.sum(valarr)
            valmoves.append([value, move])
            self.remove_move(move[0], move[1], player)
        # print(valmoves)
        sval = sorted(valmoves, key=lambda x: x[0], reverse=True)
        # print(sval)
        return [x[1] for x in sval]

    def hash_board(self):
        bstr = np.array2string(self.board, separator='')[1:-1]
        bstr = bstr.replace('3', '')
        tint = int(bstr, 3)
        return tint

    def copy(self):
        b = ChineseCheckers()
        b.board = np.copy(self.board)
        return b

    def reset(self):
        self.board = np.copy(self.board_copy)
