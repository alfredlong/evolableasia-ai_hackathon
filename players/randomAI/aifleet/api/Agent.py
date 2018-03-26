import numpy as np
from Constants import *
from Ship import *

class Agent(object):
    potentialTargetList = []
    fightMode = FightMode.HUNT
    predictionBoard = []
    shotCount = 0

    listOfShipsArray = []
    lastPlacedPoint = (np.random.random_integers(0, 1), 0)

    def __init__(self, selfBoard, enemyBoard, listOfShips):
        super(Agent, self).__init__()
        self.selfBoard = selfBoard
        self.enemyBoard = enemyBoard
        self.listOfShips = listOfShips
        self.listOfShipsArray = self.initShipsArray(listOfShips)
        self.predictionBoard = np.copy(self.enemyBoard.weightGrid)

    def initShipsArray(self, inObj):
        shipArray = []
        for key, value in inObj.iteritems():
            if key == 'CV':
                for i in xrange(value):
                    ship = Carrier()
                    shipArray.append((ship, ship.shipId + 10))
            elif key == 'BB':
                for i in xrange(value):
                    ship = Battleship()
                    shipArray.append((ship, ship.shipId + 10))
            elif key == 'CA':
                for i in xrange(value):
                    ship = Cruiser()
                    shipArray.append((ship, ship.shipId + 10))
            elif key == 'DD':
                for i in xrange(value):
                    ship = Destroyer()
                    shipArray.append((ship, ship.shipId + 10))
            elif key == 'OR':
                for i in xrange(value):
                    ship = OilRig()
                    shipArray.append((ship, ship.shipId + 10))
        return shipArray


    def tryPlaceShip(self, location, ship, color):
        ship.placedLocation = location
        rs_location = np.reshape((location[1], location[0]),(2,1))
        idx = zip(rs_location + ship.getTransposedArray())
        if self.selfBoard.checkGrid[idx].all() and not self.selfBoard.dataGrid[idx].any():
            self.selfBoard.dataGrid[idx] = color
            return True
        return False

    def placeShips(self, ships):
        for ship in ships:
            location = self.pickRandomParitySpot(self.selfBoard, ship[0].maxSize)
            while self.tryPlaceShip(location, ship[0], ship[1]) == False:
                location = self.pickRandomParitySpot(self.selfBoard, ship[0].maxSize)

    def pickRandomSpot(self, board):
        return (np.random.random_integers(0, board.n_x-1), np.random.random_integers(0, board.n_y-1))

    def pickRandomParitySpot(self, board, size):
        while self.lastPlacedPoint[0] < board.n_x:
            xVal = self.lastPlacedPoint[0]
            yVal = np.random.random_integers(0, board.n_y-1)
            self.lastPlacedPoint = (self.lastPlacedPoint[0] + size + 1, self.lastPlacedPoint[1])
            return (xVal, yVal)
        return (np.random.random_integers(0, board.n_x-1), np.random.random_integers(0, board.n_y-1))

    def pickBaseOnPrediction(self, returnNumber):
        return list(np.argwhere(self.predictionBoard.max() == self.predictionBoard))[:returnNumber]

    def huntShip(self):
        pickedList = self.pickBaseOnPrediction(1)
        # while self.checkValidCell(pickedX, pickedY, self.enemyBoard) == False:
        #     pickedX, pickedY = self.pickBaseOnPrediction(1)

        for point in pickedList:
            result = self.shotBoard(point[1], point[0])
            if result == SeaState['HIT']:
                self.fightMode = FightMode.TARGET
                self.findAndAddPotentialTargetsToList(point[1], point[0], self.enemyBoard)
            self.enemyBoard.updateCell(point[1], point[0], result)
            self.updatePredictionBoard()

    def targetShip(self):
        if len(self.potentialTargetList) > 0:
            nextX, nextY = self.potentialTargetList.pop()
            result = self.shotBoard(nextX, nextY)
            if result == SeaState['HIT']:
                self.findAndAddPotentialTargetsToList(nextX, nextY, self.enemyBoard)
            self.enemyBoard.updateCell(nextX, nextY, result)
            self.updatePredictionBoard()
        else:
            self.fightMode = FightMode.HUNT

            #TEST
            for key, value in self.listOfShips.iteritems():
                if value > 0:
                    value -= 1
                    break

            self.huntShip()


    def shotBoard(self, x, y):
        # DUMMY
        self.shotCount += 1
        if self.enemyBoard.dataGrid[int(y)][int(x)] == SeaState['CLEAR']:
            return SeaState['MISS']
        else:
            return SeaState['HIT']

    def checkValidCell(self, x, y, board):
        if x < 0 or x > board.n_x - 1:
            return False
        if y < 0 or y > board.n_y - 1:
            return False
        if board.dataGrid[int(y)][int(x)] != SeaState['CLEAR'] and board.dataGrid[int(y)][int(x)] < 10: # TEMP
            return False
        return True

    def findAndAddPotentialTargetsToList(self, startX, startY, board):
        deltaX = [0, 0, 1, -1]
        deltaY = [1, -1, 0, 0]

        # Add potential point to stack
        for i in xrange(4):
            newX = startX + deltaX[i]
            newY = startY + deltaY[i]

            if self.checkValidCell(newX, newY, board):
                self.potentialTargetList.append((newX, newY))

    def updatePredictionBoard(self):
        self.predictionBoard = np.copy(self.enemyBoard.weightGrid)
        self.applyGradientEvaluation()

    def applyGradientEvaluation(self):
        currentlistOfShips = self.initShipsArray(self.listOfShips)
        for ship in currentlistOfShips:
            for y in xrange(self.enemyBoard.n_y):
                for x in xrange(self.enemyBoard.n_x):
                    for dir in xrange(2):
                        if self.predictionBoard[int(y)][int(x)] != -1:
                            location = np.reshape((y, x),(2,1))
                            if dir == 0:
                                tArr = ship[0].getTransposedShape(ship[0].getVerticalShape())
                            else:
                                tArr = ship[0].getTransposedShape(ship[0].getHorizontalShape())
                            idx = zip(location + tArr)
                            if self.enemyBoard.checkGrid[idx].all():
                                coords = (np.asarray(ship[0].shape) + (x, y)).tolist()
                                errFlag = False
                                for coord in coords:
                                    if coord[0] >= 20 or coord[1] >= 8:
                                        errFlag = True
                                        break
                                    if self.predictionBoard[int(coord[1])][int(coord[0])] < 0:
                                        errFlag = True
                                        break
                                if errFlag: continue
                                for coord in coords:
                                    self.predictionBoard[int(coord[1])][int(coord[0])] = self.predictionBoard[int(coord[1])][int(coord[0])] + ship[1]
                        else:
                            continue
