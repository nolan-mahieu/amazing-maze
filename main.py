import random

def create_maze(n):
    maze = [['#'] * (2 * n + 1) for _ in range(2 * n + 1)]
    stack = []

    def is_valid(x, y):
        return 0 < x < 2 * n and 0 < y < 2 * n

    def has_unvisited_neighbors(x, y):
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        for nx, ny in neighbors:
            if is_valid(nx, ny) and maze[nx][ny] == '#':
                return True
        return False

    def remove_wall(x1, y1, x2, y2):
        maze[(x1+x2)//2][(y1+y2)//2] = '.'

    def recursive_backtrack(x, y):
        maze[x][y] = '.'
        stack.append((x, y))
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and maze[nx][ny] == '#':
                remove_wall(x, y, nx, ny)
                recursive_backtrack(nx, ny)

        stack.pop()

    recursive_backtrack(1, 1)
    maze[1][0] = '.'
    maze[2 * n - 1][2 * n] = '.'

    return maze

def save_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        for row in maze:
            file.write(''.join(row) + '\n')

if __name__ == "__main__":
    n = int(input("Entrez la taille du labyrinthe (un nombre impair recommandé) : "))
    maze = create_maze(n)
    filename = input("Entrez le nom du fichier pour sauvegarder le labyrinthe : ")
    save_maze_to_file(maze, filename)
    print(f"Le labyrinthe a été sauvegardé dans le fichier '{filename}'.")
