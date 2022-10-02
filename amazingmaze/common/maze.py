import numpy as np
import time
import random
from amazingmaze.common import file

class   Maze():
    
    _dic = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1),
    }

    def __init__(self, fileName = "") -> None:
        self._map = None
        self._size = -1
        self._fileName = fileName

        if fileName == "":
            self._createMap()
            self._gen(0, 0)
            self._cleanMap()
        else:
            self._loadMap()

    def _cleanMap(self, exeption = ""):
        for x in range(self._size * 2 - 1):
            for y in range(self._size * 2 - 1):
                if self._map[x][y] != '.' and self._map[x][y] != '#' and self._map[x][y] != exeption:
                    self._map[x][y] = '.'

    def _gen(self, posx, posy):
        self._map[posx][posy] = 'V'
        while True:
            dir = self._hasNeighbors(posx, posy)
            lenght = len(dir)
            if lenght == 0:
                break
            toBreak = dir.pop(dir.index(random.choice(dir)))
            self._map[posx + self._dic[toBreak][0]][posy + self._dic[toBreak][1]] = '.'
            if lenght == 1:
                posx += self._dic[toBreak][0] * 2
                posy += self._dic[toBreak][1] * 2
                self._map[posx][posy] = 'V'
            else:
                self._gen(posx + self._dic[toBreak][0] * 2, posy + self._dic[toBreak][1] * 2)

    def _hasNeighbors(self, posx, posy):
        result = []
        for dir in self._dic.keys():
            if 0 <= posx + self._dic[dir][0] < self._size * 2 - 1 and 0 <= posy + self._dic[dir][1] < self._size * 2 - 1:
                if self._map[posx + self._dic[dir][0] * 2][posy + self._dic[dir][1] * 2] == '.':
                    result.append(dir)
        return result

    def _mapFromText(self, content, size):
        x, posx, posy = 0, 0, 0
        length = len(content)
        while content[x] != '\n':
            x += 1
        x += 2
        for posx in range(size):
            for posy in range(size):
                self._map[posx][posy] = content[x]
                if content[x + 2] == '\n':
                    if content[x + 1] == '.':
                        break
                    else:
                        x += 4
                else:
                    x += 1

    def _loadMap(self):
        content = file.readFile(self._fileName)
        for x in range(len(content)):
            if content[x] == "\n":
                break
        self._size = x
        self._size = int((self._size - 1) / 2)
        size = self._size + self._size - 1
        self._map = np.zeros((size, size), dtype=str)
        np.set_printoptions(threshold=np.inf)
        self._mapFromText(content, size)

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
        content = self._mapToText()
        en = time.time()
        print("To str in :", en - st, "'s")
        #print(content)
        file.writeFile(self._fileName, content, "wt")

    def printMap(self):
        print(self._mapToText())