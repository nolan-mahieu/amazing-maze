import sys
import os
root_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_directory)

from classes.Maze import *
from classes.Solver import *

def get_generator(generation: str):
    folder = './generator/maze_generated/' + generation
    name = input("Enter the name of maze for solving : ")
    path_file = os.path.join(folder, name)
    if not path_file.endswith(".txt"):
        path_file += ".txt"
    if os.path.exists(path_file):
        with open(path_file, 'r') as file:
            content = file.read()
        lines = content.split('\n')
        board= [list(line) for line in lines]
        solver = Solver(board)
        solver.choosing_solver()
    else:
        print(f"The file {path_file} doesn't exist.")

def start():
    while True:
        print(' ')
        print("Chooze your generation maze")
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
            get_generator("kruskal")
        elif number == "2":
            get_generator("backtracking")
        elif number == "3":
            break
        else:
            print(' ')
            print('Enter a valid number !')
            print(' ')
            
start()