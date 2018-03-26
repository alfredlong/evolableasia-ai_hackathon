class GameStatus(object):

    def __init__(self, opp_player, my_player, turn, opp_board, my_board, strategy):
        # player
        self.opp_player = opp_player
        self.my_player = my_player
        # turn
        self.turn = turn
        # board
        self.opp_board = opp_board
        self.my_board = my_board
        # strategy
        self.strategy = strategy

    def __str__(self):
        opp_board_str = '\n'
        for i in range(0, len(self.opp_board)):
            for j in range(0, len(self.opp_board[i])):
                opp_board_str += '(%d, %d): %s ' % (i, j, self.opp_board[i][j])
                if j == len(self.opp_board[i]) - 1:
                    opp_board_str += '\n'

        my_board_str = '\n'
        for i in range(0, len(self.my_board)):
            for j in range(0, len(self.my_board[i])):
                my_board_str += '(%d, %d): %s ' % (i, j, self.my_board[i][j])
                if j == len(self.my_board[i]) - 1:
                    my_board_str += '\n'

        strategy_str = '\n' + str(self.strategy.mode) + "\n"
        for key, value in self.strategy.grid_points.items():
            strategy_str += str(key) + ' ' + str(value) + '\n'

        return 'opp_player:' + str(self.opp_player) + '\n' \
               'my_player:' + str(self.my_player) + '\n' \
               'opp: ' + opp_board_str + '\n' + \
               'my: ' + my_board_str + '\n' + 'strategy_str:' + strategy_str

    class Meta:
        pass
