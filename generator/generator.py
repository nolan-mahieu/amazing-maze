import sys
import os
root_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_directory)
from classes.Maze import *

def generation_maze(generation: str):
    name = input('Enter the desired filename (without extension): ')
    size = int(input('Enter a size for maze: '))
    maze = Maze(name, size)
    if generation == "kruskal":
        maze.kruskal()
    elif generation == "backtracking":
        maze.backtracking()
    maze_text = maze.print_maze()
    maze.save_file(name, maze_text, generation)

def start():
    while True:
        print(' ')
        print("Chooze maze generation algorithm")
        print("1 - Kruskal's algorithm")
        print('2 - Backtracking algorithm')
        print('3 - Leave')
        print(' ')
        number = input('Enter a number > ')
        print(' ')
        if number.isdigit() == False:
            print(' ')
            print('Enter a number between 1 and 2 !')
            print(' ')
        elif number == "1":
            generation_maze("kruskal")
        elif number == "2":
            generation_maze("backtracking")
        elif number == "3":
            break
        else:
            print(' ')
            print('Enter a valid number !')
            print(' ')
            
start()