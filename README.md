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
