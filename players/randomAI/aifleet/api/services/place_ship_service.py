from .cache_services import CacheService
from django.conf import settings
from random import randint
from .strategy_service import StrategyService
from ..domains.plot_status import PlotStatus
from ..domains.game_status import GameStatus
from ..domains.strategy import Strategy
from ..domains.ship_models import ShipModel


class PlaceShipsService:

    @staticmethod
    def setup_game(player1, player2, session_id):
        # get game rule
        game_rule = CacheService.get(settings.GAME_RULE_CACHE_PREFIX, session_id)

        if not game_rule:
            # could not get game rule, return false
            return False, []

        # draw boards (prepare data for coordinates)
        game_status = PlaceShipsService.draw_board(game_rule, player1, player2)

        # arrange our ships on our board
        ships = PlaceShipsService.arrange_ships(game_rule, game_status)

        # Set game status to cache
        CacheService.set(settings.GAME_STATUS_CACHE_PREFIX, session_id, game_status)

        return True, ships

    @staticmethod
    def arrange_ships(game_rule, game_status):
        ships = []
        board_width = game_rule.get('boardWidth')
        board_height = game_rule.get('boardHeight')

        # arrange ships loop
        for ship_model in game_rule.get('ships'):
            ship_type = ship_model.get('type')
            quantity = ship_model.get('quantity')
            for i in range(quantity):
                # arrange this type of ship
                success = False
                count = 0 # max count = 20
                max_count = 20
                while success is False and count < max_count:
                    # plot ship until success
                    # get pos info
                    pos_info = ShipModel.get_pos(ship_type)

                    width = pos_info.get('width')
                    height = pos_info.get('height')

                    x = randint(0, board_width - width)
                    y = randint(0, board_height - height)

                    if PlaceShipsService.check_ship(x, y, width, height, board_width, board_height, game_status):
                        # update game_status
                        coordinates = PlaceShipsService.update_game_status_with_ships(x, y, pos_info, game_status)
                        # create ship and add to list
                        ships.append({'type': ship_type, 'coordinates': coordinates})
                        success = True
        return ships

    # check if the ship is placed well or not
    @staticmethod
    def check_ship(x, y, width, height, board_width, board_height, game_status):
        min_x = x
        if min_x > 0:
            if randint(0, 1) == 0:
                min_x = x - 1
        max_x = x + width
        if max_x < board_width - 1:
            if randint(0, 1) == 0:
                max_x = max_x + 1

        min_y = y
        if min_y > 0:
            if randint(0, 1) == 0:
                min_y = y - 1

        max_y = y + height
        if max_y < board_height - 1:
            if randint(0, 1) == 0:
                max_y = max_y + 1

        # check if overlap with another ship or not
        for i in range(min_x, max_x):
            for j in range(min_y, max_y):
                if game_status.my_board[i][j].has_ship:
                    return False
        return True

    @staticmethod
    def update_game_status_with_ships(x, y, pos_info, game_status):
        # position of new ship
        coordinates = []

        for each in pos_info.get('pos'):
            tmp_plot = game_status.my_board[x + each[0]][y + each[1]]
            game_status.my_board[x + each[0]][y + each[1]] = PlotStatus(tmp_plot.hit_status, True, tmp_plot)
            coordinates.append([x + each[0], y + each[1]])

        return coordinates

    @staticmethod
    def draw_board(game_rule, player1, player2):
        # get board size
        board_width = game_rule.get('boardWidth')
        board_height = game_rule.get('boardHeight')

        # initialize turn
        turn = 0

        # opp board data
        opp_board = [[PlotStatus(PlotStatus.FREE, False, 1.0) for y in range(board_height)]
                     for x in range(board_width)]
        # my board data
        my_board = [[PlotStatus(PlotStatus.FREE, False, 1.0) for y in range(board_height)]
                    for x in range(board_width)]

        # create list of free points
        free_points = [[x, y] for x in range(board_width) for y in range(board_height)]

        # strategy data
        strategy = Strategy(mode=Strategy.GRID_SEARCH, level=0,
                            grid_points=[],
                            tracing_points=[], free_points=free_points, hit_points=[],
                            remain_ships=game_rule.get('ships'))

        # set player ids
        if player1 == settings.MY_PLAYER_ID:
            my_player = player1
            opp_player = player2
        else:
            my_player = player2
            opp_player = player1

        # game status
        game_status = GameStatus(turn=turn, opp_player=opp_player, my_player=my_player,
                                 opp_board=opp_board, my_board=my_board, strategy=strategy)

        return game_status

    @staticmethod
    def create_response(ships):
        return {'ships': ships}