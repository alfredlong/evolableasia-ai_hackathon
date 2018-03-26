from rest_framework import serializers
from .ship_type import ShipType, ShipTypeSerializer


# game rule
class GameRule(object):
    def __init__(self, boardWidth, boardHeight, ships):
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.ships = ships

    def __str__(self):
        display = 'boardWidth: %(boardWidth)d, boardHeight: %(boardHeight)d' % \
               {'boardWidth': self.boardWidth, 'boardHeight': self.boardHeight}
        ships_display = ' '.join(['type: %(type)s quantity: %(quantity)d' %
                                  {'type': each.type, 'quantity': each.quantity} for each in self.ships])
        return display + ' ' + ships_display

    class Meta:
        pass


# serializer
class GameRuleSerializer(serializers.Serializer):
    boardWidth = serializers.IntegerField()
    boardHeight = serializers.IntegerField()
    ships = ShipTypeSerializer(many=True)

    def create(self, validated_data):
        game_rule = GameRule(**validated_data)
        ships_data = validated_data.pop('ships')
        game_rule.ships = [ShipType(each['type'], each['quantity']) for each in ships_data]
        return game_rule

    def update(self, instance, validated_data):
        return instance
