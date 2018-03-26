from random import randint


class Direction(object):
    VERTICAL = 1
    HORIZONTAL = 2


class ShipModel(object):
    SMALL_SHIP_SIZE = 2
    DEF_POS = {
        'PT': {
            Direction.HORIZONTAL: {'pos': [(0, 0)], 'width': 1, 'height': 1},
            Direction.VERTICAL: {'pos': [(0, 0)], 'width': 1, 'height': 1},
        },
        'DD': {
            Direction.HORIZONTAL: {'pos': [(0, 0), (1, 0)], 'width': 2, 'height': 1},
            Direction.VERTICAL: {'pos': [(0, 0), (0, 1)], 'width': 1, 'height': 2},
        },
        'CA': {
            Direction.HORIZONTAL: {'pos': [(0, 0), (1, 0), (2, 0)], 'width': 3, 'height': 1},
            Direction.VERTICAL: {'pos': [(0, 0), (0, 1), (0, 2)], 'width': 1, 'height': 3},
        },
        'OR': {
            Direction.HORIZONTAL: {'pos': [(0, 0), (1, 0), (0, 1), (1, 1)], 'width': 2, 'height': 2},
            Direction.VERTICAL: {'pos': [(0, 0), (1, 0), (0, 1), (1, 1)], 'width': 2, 'height': 2},
        },
        'BB': {
            Direction.HORIZONTAL: {'pos': [(0, 0), (1, 0), (2, 0), (3, 0)], 'width': 4, 'height': 1},
            Direction.VERTICAL: {'pos': [(0, 0), (0, 1), (0, 2), (0, 3)], 'width': 1, 'height': 4},
        },
        'CV': {
            Direction.HORIZONTAL: {'pos': [(1, 0),
                                     (0, 1), (1, 1), (2, 1), (3, 1)], 'width': 4, 'height': 2},
            Direction.VERTICAL: {'pos': [(1, 0),
                                 (0, 1), (1, 1),
                                         (1, 2),
                                         (1, 3)], 'width': 2, 'height': 4},
        }
    }

    @staticmethod
    def get_pos(type_name):
        # randomly the shape
        return ShipModel.DEF_POS.get(type_name, None).get(randint(Direction.VERTICAL, Direction.HORIZONTAL))

    @staticmethod
    def cal_dif(base_point, des_point):
        dif_point = (des_point[0] - base_point[0], des_point[1] - base_point[1])
        return dif_point

    @staticmethod
    def cal_sum(base_point, vector):
        sum_point = (vector[0] + base_point[0], vector[1] + base_point[1])
        return sum_point



