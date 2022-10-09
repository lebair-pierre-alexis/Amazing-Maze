import random
from amazingmaze.common import maze

def run():

    fileName = ""

    while True:
        try:
            size = int(input("Enter the size of the maze (enter -1 in case you want to load a existing maze) : "))
        except ValueError:
            print("Enter a valide number (either -1 or a positive number")
            continue
        if size != -1 and size < 0:
            print("Enter a valide number (either -1 or a positive number")
            continue
        elif size == -1:
            fileName = input("You choose to open a existing maze, please enter it's name :")
            break
        else:
            break

    map = maze.Maze(size, fileName)
    #map.loadMap()
    if fileName == "":
        x, y = random.randrange(0, size), random.randrange(0, size)
        map.gen(0, 0)
    map.printMap()
    map.mapToFile()
