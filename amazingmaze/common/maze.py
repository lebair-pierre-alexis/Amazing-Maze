from math import sqrt
import numpy as np
import random
from amazingmaze.common import file


class   Cell():

    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def hasWalls(self):
        return all(self.walls.values())

    def breakWall(self, other, wall):
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

class   Maze():

    delta = [('W', (0, -1)),
             ('E', (0, 1)),
             ('S', (1, 0)),
             ('N', (-1, 0))]

    def __init__(self, size = 0, fileName = "") -> None:
        self._fileName = fileName
        if size != -1:
            self._map = [[Cell(x, y) for y in range(size)] for x in range(size)]
            self._size = size * size
        else:
            self.loadMap()

    def _cellAt(self, x, y):
        return self._map[x][y]

    def _findValidNeighbour(self, cell:Cell):
        neighbours = []
        for direction, (dx, dy) in self.delta:
            x2, y2 = cell._x + dx, cell._y + dy
            if 0 <= x2 < int(sqrt(self._size)) and 0 <= y2 < int(sqrt(self._size)):
                neighbour = self._cellAt(x2, y2)
                if neighbour.hasWalls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def gen(self, x, y):
        cellStack = []
        currentCell = self._cellAt(x, y)
        visited = 1
        size = int(sqrt(self._size))

        while visited < self._size:
            neighbours = self._findValidNeighbour(currentCell)
            if not neighbours:
                currentCell = cellStack.pop()
                continue
            direction, nextCell = random.choice(neighbours)
            currentCell.breakWall(nextCell, direction)
            cellStack.append(currentCell)
            currentCell = nextCell
            visited += 1
        self._map[size - 1][size - 1].walls["E"] = False
        self._map[0][0].walls["W"] = False

    def loadMap(self):
        content = file.readFile(self._fileName)
        for size, x in enumerate(content):
            if x == '\n':
                break
        self._size = int(((size - 1) / 2)**2)
        self._map = [[Cell(x, y) for y in range(int(sqrt(self._size)))] for x in range(int(sqrt(self._size)))]
        content = content.splitlines()
        for x, line in enumerate(content):
            if x and x != len(line) - 1:
                for y, l in enumerate(line):
                    if y != 0 and y != len(line) - 1:
                        if x % 2:
                            if y % 2 == 0 and l == ".":
                                self._map[int(x / 2)][int(y / 2) - 1].walls["E"] = False
                                self._map[int(x / 2)][int(y / 2)].walls["W"] = False
                        else:
                            if y % 2 and l == ".":
                                self._map[int(x / 2) - 1][int(y / 2)].walls["S"] = False
                                self._map[int(x / 2)][int(y / 2)].walls["N"] = False

    def _mapToText(self):
        size = int(sqrt(self._size))
        mapText = "." + "".join(("#" for x in range(size * 2))) + "\n"
        for x, line in enumerate(self._map):
            if x:
                mapText += '#'
            else:
                mapText += '.'
            wall = ""
            if x != int(sqrt(self._size)) - 1:
                wall += "\n#"
            for y, cell in enumerate(line):
                mapText += '.'
                if cell.walls['E'] and (x != int(sqrt(self._size)) - 1 or y != int(sqrt(self._size)) - 1):
                    mapText += '#'
                else:
                    mapText += '.'
                if x != int(sqrt(self._size)) - 1:
                    if cell.walls['S']:
                        wall += "##"
                    else:
                        wall += ".#"
            mapText += wall + '\n'
        mapText += "".join("#" for x in range(size * 2)) + "."
        return mapText


    def mapToFile(self):
        content = self._mapToText()
        if self._fileName == "":
            fileName = input("Entrez le nom du fichier dans lequel enregistrer le labyrinthe : ")
        file.writeFile(fileName, content, "wt")

    def printMap(self):
        print(self._mapToText())