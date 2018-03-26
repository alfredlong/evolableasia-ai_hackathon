from enum import Enum

SeaState = {
    'CLEAR': 0,
    'MISS': 3,
    'HIT': 5,
    'SUNK': 7,
}

class FightMode(Enum):
    HUNT = 0
    TARGET = 1

class Orientation(Enum):
    VERTICAL = 0
    HORIZONTAL = 1
