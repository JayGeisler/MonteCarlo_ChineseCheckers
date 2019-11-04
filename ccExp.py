from ccPlayer import MC_Player, Ordered_Player, Random_Player
from ccBoard import ChineseCheckers
'''
where 2 players and the board will be init and then play a game 
ime limit will be set on each player 
'''

import numpy as np
#import matplotlib.pyplot as plt

BLACK = 1
WHITE = 2


def experiment():
    cc = ChineseCheckers()
    # cc.print_values()
    # return
    p1 = MC_Player(BLACK)
    p2 = Ordered_Player(WHITE)
    c = 0
    moves = cc.move_ordering(BLACK)
    values = np.zeros(len(moves))
    count = np.zeros(len(moves))
    cc.print_graph_board()
    for x in range(10):
        cc.reset()
        cc.update_graph_board()
        winner = 0
        eps = np.random.uniform()
        if eps > 0.5:
            move_i = np.argmax(values)
            move = moves[move_i]
            cc.play_move(move[0], move[1], BLACK)
        else:
            move_i = np.random.randint(len(moves))
            move = moves[move_i]
            cc.play_move(move[0], move[1], BLACK)

        count[move_i] += 1
        while(c < 50):
            c += 1
            p2.play_move(cc)
            cc.update_graph_board()
            if cc.terminal() == WHITE:
                winner = WHITE
                print("White wins", c)
                break
            p1.play_move(cc)
            cc.update_graph_board()
            if cc.terminal() == BLACK:
                print("Black wins", c)
                winner = BLACK
                break
        if winner == BLACK:
            values[move_i] = values[move_i] + \
                (1-values[move_i])/(count[move_i])
        else:
            values[move_i] = values[move_i] + \
                (0-values[move_i])/(count[move_i])
        c = 0



experiment()
