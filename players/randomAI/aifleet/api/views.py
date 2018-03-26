from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.invite_services import InviteService
from .services.place_ship_service import PlaceShipsService
from .services.shoot_service import ShootService
from .services.validate_service import ValidateService

import numpy as np
import matplotlib.pyplot as plt
from Board import Board
from Agent import Agent
from Ship import *
from Constants import *

myBoard = None
enemyBoard = None
agent = None

class Invite(APIView):
    def post(self, request, format=None):
        # get session_id and token from header
        session_id = self.request.META.get('HTTP_X_SESSION_ID')
        token = self.request.META.get('HTTP_X_TOKEN')
        return_headers = {'X-SESSION-ID':session_id, 'X-TOKEN':token}

        print ("session id:", session_id)
        print ("token:", token)

        # game rule data
        game_rule_data = request.data
        # validate game rule
        valid = ValidateService.validate_game_rule(game_rule_data)
        if valid:
            # prepare game info by putting game rule to cache
            result = InviteService.prepare_game(game_rule_data, session_id)

        # invalid request
        if not valid or not result:
            return Response(headers=return_headers, status=status.HTTP_400_BAD_REQUEST)

        return Response(headers=return_headers, status=status.HTTP_200_OK)


class PlaceShips(APIView):
    def post(self, request, format=None):
        # get session_id and token from header
        session_id = self.request.META.get('HTTP_X_SESSION_ID')
        token = self.request.META.get('HTTP_X_TOKEN')
        return_headers = {'X-SESSION-ID': session_id, 'X-TOKEN': token}

        # get player id
        player1 = request.data['player1']
        player2 = request.data['player2']
        if player1 and player2:
            # setup game
            result, ships = PlaceShipsService.setup_game(player1, player2, session_id)
            # in case of invalid
            if not result:
                return Response(headers=return_headers, status=status.HTTP_400_BAD_REQUEST)

            response_data = PlaceShipsService.create_response(ships)
            return Response(headers=return_headers, data=response_data, status=status.HTTP_200_OK)

        return Response(headers=return_headers, status=status.HTTP_400_BAD_REQUEST)


class Shoot(APIView):
    def post(self, request, format=None):
        # get session_id and token from header
        session_id = self.request.META.get('HTTP_X_SESSION_ID')
        token = self.request.META.get('HTTP_X_TOKEN')
        return_headers = {'X-SESSION-ID': session_id, 'X-TOKEN': token}

        # validate
        # TODO

        turn_number = request.data['turn']
        max_shots = request.data['maxShots']

        # get game status and check valid turn
        game_status, game_rule, check_result = ShootService.get_game_status(session_id, turn_number)
        if not check_result:
            return Response(headers=return_headers, data='invalid turn', status=status.HTTP_400_BAD_REQUEST)

        # calculate next fire point
        print(max_shots)
        fire_points = []
        for i in range(max_shots):
            fire_point = ShootService.shoot(game_status, game_rule)
            fire_points.append(fire_point)

        print (fire_points)
        # update game status
        ShootService.update_game_status(fire_points, game_status, session_id)

        response_data = ShootService.create_response(fire_points)

        return Response(headers=return_headers, data=response_data, status=status.HTTP_200_OK)


class NotifyShotResult(APIView):
    def post(self, request, format=None):
        # get session_id and token from header
        session_id = self.request.META.get('HTTP_X_SESSION_ID')
        token = self.request.META.get('HTTP_X_TOKEN')
        return_headers = {'X-SESSION-ID': session_id, 'X-TOKEN': token}

        data = self.request.data
        player = data.get('playerId', None)
        shots = data.get('shots', None)
        sunk_ships = data.get('sunkShips', None)

        print (player, shots, sunk_ships)

        return Response(headers=return_headers, data={}, status=status.HTTP_200_OK)


class GameOver(APIView):
    def post(self, request, format=None):
        # get session_id and token from header
        session_id = self.request.META.get('HTTP_X_SESSION_ID')
        token = self.request.META.get('HTTP_X_TOKEN')
        return_headers = {'X-SESSION-ID': session_id, 'X-TOKEN': token}

        data = self.request.data
        winner = data.get('winner', None)
        loser = data.get('loser', None)
        statistics = data.get('statistics', None)

        print(winner, loser, statistics)

        return Response(headers=return_headers, data='', status=status.HTTP_200_OK)
