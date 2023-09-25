from classes.Cell import Cell
import random
import os

class Maze:
    def __init__(self, name: str, n: int):
        self.name = name
        self.n = n
        self.board = [[Cell((i,j)) for j in range(self.n)] for i in range(self.n)]
        self.entrance = self.get_cell(0,0)
        self.sets = list(range(self.n * self.n)) 

    def get_cell(self, x: int,  y: int):
        return self.board[x][y]
    
    def backtracking(self):
        current_cell = self.entrance
        current_cell.visited = True
        iteration = 0
        stack = [current_cell]
        while iteration < self.n * self.n:
            neighbors = current_cell.get_neighbors(self.n)
            unvisited_neighbors = [neighbor for neighbor in neighbors if not self.get_cell(neighbor[0][0], neighbor[0][1]).visited]
            if unvisited_neighbors:
                random_neighbor = random.choice(unvisited_neighbors)
                next_cell = self.get_cell(random_neighbor[0][0], random_neighbor[0][1])
                direction = random_neighbor[1]
                next_cell.visited = True
                current_cell.break_wall(next_cell, direction)
                stack.append(next_cell)
                current_cell = next_cell
            else:
                if stack:
                    current_cell = stack.pop()
                    iteration -= 1                
            iteration += 1

    def kruskal(self):
        edges = []
        for row in range(self.n):
            for col in range(self.n):
                cell = self.board[row][col]
                neighbors = cell.get_neighbors(self.n)
                for neighbor, direction in neighbors:
                    edges.append((cell, self.get_cell(neighbor[0], neighbor[1]), direction))
        random.shuffle(edges)
        for edge in edges:
            cell1, cell2, direction = edge
            set1 = self.sets[cell1.pos[0] * self.n + cell1.pos[1]]
            set2 = self.sets[cell2.pos[0] * self.n + cell2.pos[1]]
            if set1 != set2:
                min_set = min(set1, set2)
                max_set = max(set1, set2)
                for i in range(self.n * self.n):
                    if self.sets[i] == max_set:
                        self.sets[i] = min_set
                cell1.break_wall(cell2, direction)
                cell1.visited = True
                cell2.visited = True

    def print_maze(self):
        maze_display = [["#" for _ in range(2 * self.n +1)] for _ in range(2 * self.n + 1)]
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col].visited == True:
                    maze_display[2 * row + 1][2 * col + 1] = "."
                if self.board[row][col].walls['N']:
                    maze_display[2 * row][2 * col + 1] = "#"
                else:
                    maze_display[2 * row][2 * col + 1] = "."
                if self.board[row][col].walls['S']:
                    maze_display[2 * row + 2][2 * col + 1] = "#"
                else:
                    maze_display[2 * row + 2][2 * col + 1] = "."
                if self.board[row][col].walls['W']:
                    maze_display[2 * row + 1][2 * col] = "#"
                else:
                    maze_display[2 * row + 1][2 * col] = "."
                if self.board[row][col].walls['E']:
                    maze_display[2 * row + 1][2 * col + 2] = "#"
                else:
                    maze_display[2 * row + 1][2 * col + 2] = "."
        maze_display[0][0] = "."
        maze_display[1][0] = "."
        maze_display[2*self.n][2*self.n] = "."
        maze_display[2*self.n - 1][2*self.n] = "."
        maze_str = ""
        count = 0
        for line in maze_display:
            if count == len(maze_display)-1:
                maze_str += "".join(line)
            else:
                maze_str += "".join(line) + '\n'
            count+=1
        return maze_str
    
    def save_file(self, name: str, maze_text: str, generation: str):
        folder_maze = './generator/maze_generated/' + generation
        name_with_underscores = name.replace(' ', '_')
        if not os.path.exists(folder_maze):
            os.makedirs(folder_maze)
        name_file =  os.path.join(folder_maze, f'{name_with_underscores}.txt')
        with open(name_file, 'w') as file:
            file.write(maze_text)
        print(f'The labyrinth was registered under the name {name_file}')
