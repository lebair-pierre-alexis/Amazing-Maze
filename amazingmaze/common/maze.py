import numpy as np

class   Maze():
    
    def __init__(self, fileName = "") -> None:
        self._map = None
        self._size = -1

        if fileName == "":
            self._createMap()

    def _mapFromSize(self, size):
        self._map = np.zeros((size, size), dtype=int)
        for x in range(size):
            for y in range(size):
                if x % 2 != 0 or y % 2 != 0:
                    self._map[x][y] = 1
                else:
                    self._map[x][y] = 0

    def _createMap(self):
        self._size = input("Please entre the size of the maze : ")
        while self._size.isdigit() == False:
            self._size = input("The size must be a number, please enter a valid size : ")
        self._size = int(self._size)
        self._mapFromSize(self._size + self._size - 1)

    def mapToText(self, map):
        pass