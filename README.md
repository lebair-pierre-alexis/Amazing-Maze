# Amazing-Maze
    Amazing-Maze is a maze generator and maze solver project that takes part in our first year in La Plateforme.
    The program will either generate a maze, or solve one, using differents algorithm (choosed by the user).
    The maze is displayed in a file : name.mz.txt and the solved maze in : name.sv.txt.
    The entrance will always be at the top left corner and the exit at the bottom right corner.
    Rooms and destroyed walls are represented by a '.' and walls are represented by a '#'
    For the maze generation the user will be prompted to enter the desired size of the maze and a file name to save it into

# How to run this project
    You may run this project by typing :
    python -m amazingmaze

# Project Structure
    The entire project is considered and launched as a python package :

        - main.py :
            Contains the basic logic and loop for the program

        - file.py :
            Contains functions related to file handling

        - maze.py :
            This file contains the Maze class and all its methods such as generation, converting to text in order to write a file, loading the maze from an existing file

# The underlying magic !
    The Maze class, upon instantiation, will either take a file name or nothing.
    If nothing is passed to the constructor it will understand that we are generating a new maze and therefore ask the user for a size and later a name for the file to save the maze into.
    If a file name is given, it will load the maze in memory.

    The maze itself is a bit shorter than the actual one that is displayed in the file.
    for exemple a maze (before breaking any walls) of size 3 will look like this :

        .######
        ..#.#.#
        #######
        #.#.#.#
        #######
        #.#.#..
        ######.

    When in the actual class it is stored as a numpy array with 0 for rooms and 1 for walls and is looking like this :

        .#.#.
        #####
        .#.#.
        #####
        .#.#.

    This will prevent the generation and solving algorithm from performing operations on useless part of the maze since all the maze contour will never change nor be modified by the algorithm