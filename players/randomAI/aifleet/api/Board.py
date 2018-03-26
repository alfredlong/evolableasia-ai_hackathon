import numpy as np
import matplotlib.pyplot as plt
from Constants import *

class Board(object):
    dataGrid = np.zeros((0, 0))
    checkGrid = np.zeros((0, 0))
    weightGrid = np.zeros((0, 0))
    maxShipLength = 4
    n_time = 1

    def __init__(self, n_x, n_y):
        super(Board, self).__init__()
        self.n_x = n_x
        self.n_y = n_y
        self.initDataGrid();

    def initDataGrid(self):
        self.dataGrid = np.zeros((self.n_y, self.n_x))
        self.weightGrid = np.zeros((self.n_y, self.n_x))
        self.checkGrid = np.zeros((self.n_y + self.maxShipLength, self.n_x + self.maxShipLength))
        self.checkGrid[:self.n_y,:self.n_x] = 1

    def drawBoard(self):
        self.plot = plt.matshow(self.dataGrid, interpolation='nearest')
        ax = plt.gca()
        ax.set_xticks(np.arange(-.5, self.n_x, 1));
        ax.set_yticks(np.arange(-.5, self.n_y, 1));
        ax.set_xticklabels(np.arange(0, self.n_x + 1, 1))
        ax.set_yticklabels(np.arange(0, self.n_y + 1, 1))
        plt.grid()
        plt.show(block=False)

    def resetBoard(self):
        self.dataGrid = np.zeros((0, 0))
        self.checkGrid = np.zeros((0, 0))
        self.initDataGrid()
        plt.clf()

    def updateCell(self, x, y, value):
        print('Shot at X=%d, Y=%d, value=%d' % (x, y, value))
        self.dataGrid[int(y)][int(x)] = value
        self.weightGrid[int(y)][int(x)] = -9999
        self.plot.set_data(self.dataGrid)
        plt.pause(.01)
        plt.draw()
