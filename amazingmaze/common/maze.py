import numpy as np
import time
from amazingmaze.common import file

class   Maze():
    
    def __init__(self, fileName = "") -> None:
        self._map = None
        self._size = -1
        self._fileName = fileName

        if fileName == "":
            self._createMap()

    def _loadMap(self):
        content = file.readFile(self._fileName)
        for x in range(len(content)):
            if content[x] == "\n":
                break
            self._size = x
        self._size = (self._size - 1) / 2

    def _mapFromSize(self, size):
        self._map = np.zeros((size, size), dtype=str)
        np.set_printoptions(threshold=np.inf)
        for x in range(size):
            for y in range(size):
                if x % 2 != 0 or y % 2 != 0:
                    self._map[x][y] = "#"
                else:
                    self._map[x][y] = "."

    def _createMap(self):
        self._size = input("Please entre the size of the maze : ")
        while self._size.isdigit() == False:
            self._size = input("The size must be a number, please enter a valid size : ")
        self._size = int(self._size)
        self._mapFromSize(self._size + self._size - 1)

    def _mapToText(self):
        mapText = ""
        for x in range(self._size + self._size + 1):
            if x == 0:
                mapText += "."
            else:
                mapText += "#"
        mapText += "\n"
        for x in range(self._size + self._size - 1):
            for y in range(self._size + self._size + 1):
                if (x == 0 and y == 0) or (x == self._size + self._size - 2 and y == self._size + self._size):
                    mapText += "."
                elif y == 0 or y == self._size + self._size:
                    mapText += "#"
                else:
                    mapText += self._map[x][y - 1]
            mapText += "\n"
        for x in range(self._size + self._size + 1):
            if x == self._size + self._size:
                mapText += "."
            else:
                mapText += "#"
        return mapText
    
    def _mapToText2(self):
        mapText = "." + "".join(("#" for x in range(self._size + self._size))) + "\n"
        for x in range(self._size + self._size - 1):
            if x == 0:
                mapText += "." + str(self._map[x])[1:-1].replace("'", "").replace(" ", "").replace("\n", "") + "#\n"
            elif x == self._size + self._size - 2:
                mapText += "#" + str(self._map[x])[1:-1].replace("'", "").replace(" ", "").replace("\n", "") + ".\n"
            else:
                mapText += "#" + str(self._map[x])[1:-1].replace("'", "").replace(" ", "").replace("\n", "") + "#\n"
        mapText += "".join("#" for x in range(self._size + self._size)) + "."
        return mapText

    def mapToFile(self):
        st = time.time()
        print("start")
        content = self._mapToText2()
        en = time.time()
        print("To str in :", en - st, "'s")
        #print(content)
        file.writeFile(self._fileName, content, "wt")

    def printMap(self):
        print(self._mapToText())