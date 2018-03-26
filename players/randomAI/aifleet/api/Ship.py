import numpy as np
from Constants import *

# CV = carrier
# BB = battleship
# CA = cruiser
# DD = destroyer
# OR = oil rig

class Ship(object):
    appendix = 'None'
    orientation = Orientation.VERTICAL
    shape = []
    placedLocation = []
    shipId = None
    maxSize = 0

    def __init__(self):
         super(Ship, self).__init__()
         self.orientation = Orientation.VERTICAL

    def getAppendix(self):
        return self.appendix

    def randomPickOrientation(self):
        random = np.random.random_integers(0,1)
        if random == 0:
            print('Vertical')
            return Orientation.VERTICAL
        print('Horizontal')
        return Orientation.HORIZONTAL

    def getNormalCoordinates(self):
        return self.shape

    def getPlacedCoordinates(self):
        return (np.asarray(self.shape) + self.placedLocation).tolist()

    def getTransposedArray(self):
        numpyArray = np.array(self.shape)
        return np.flip(np.transpose(numpyArray), 0)

    def getTransposedShape(self, array):
        numpyArray = np.array(array)
        return np.flip(np.transpose(numpyArray), 0)

class Carrier(Ship):
    appendix = 'CV'
    shipId = 4
    maxSize = 2

    def __init__(self):
        Ship.__init__(self)
        self.initShape()

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            self.shape = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 1]]
        else:
            self.shape = [[0, 1], [1, 1], [2, 1], [3, 1], [2, 0]]

    def getVerticalShape(self):
        return [[0, 0], [0, 1], [0, 2], [0, 3], [1, 1]]

    def getHorizontalShape(self):
        return [[0, 1], [1, 1], [2, 1], [3, 1], [2, 0]]

class Battleship(Ship):
    appendix = 'BB'
    shipId = 0
    maxSize = 1

    def __init__(self):
        Ship.__init__(self)
        self.initShape()

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            self.shape = [[0, 0], [0, 1], [0, 2], [0, 3]]
        else:
            self.shape = [[0, 0], [1, 0], [2, 0], [3, 0]]

    def getVerticalShape(self):
        return [[0, 0], [0, 1], [0, 2], [0, 3]]

    def getHorizontalShape(self):
        return [[0, 0], [1, 0], [2, 0], [3, 0]]

class Cruiser(Ship):
    appendix = 'CA'
    shipId = 2
    maxSize = 1

    def __init__(self):
        Ship.__init__(self)
        self.initShape()

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            self.shape = [[0, 0], [0, 1], [0, 2]]
        else:
            self.shape = [[0, 0], [1, 0], [2, 0]]

    def getVerticalShape(self):
        return [[0, 0], [0, 1], [0, 2]]

    def getHorizontalShape(self):
        return [[0, 0], [1, 0], [2, 0]]

class Destroyer(Ship):
    appendix = 'DD'
    shipId = 1
    maxSize = 1

    def __init__(self):
        Ship.__init__(self)
        self.initShape()

    def initShape(self):
        if self.orientation == Orientation.VERTICAL:
            self.shape = [[0, 0], [0, 1]]
        else:
            self.shape = [[0, 0], [1, 0]]

    def getVerticalShape(self):
        return [[0, 0], [0, 1]]

    def getHorizontalShape(self):
        return [[0, 0], [1, 0]]

class OilRig(Ship):
    appendix = 'OR'
    shipId = 5
    maxSize = 2

    def __init__(self):
        Ship.__init__(self)
        self.initShape()

    def initShape(self):
        self.shape = [[0, 0], [0, 1], [1, 0], [1, 1]]

    def getVerticalShape(self):
        return [[0, 0], [0, 1], [1, 0], [1, 1]]

    def getHorizontalShape(self):
        return [[0, 0], [0, 1], [1, 0], [1, 1]]
