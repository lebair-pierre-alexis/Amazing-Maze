import sys
from amazingmaze.common import maze

sys.setrecursionlimit(10**5)

def run():
    map = maze.Maze()
    map.printMap()
    map.mapToFile()
