class Cell():
    def __init__(self, pos: tuple):
        self.pos = pos
        self.walls = {"N": True, "E": True, "S": True, "W": True}
        self.visited = False

    def break_wall(self, next_cell: 'Cell', direction: str):
        opposition_direction = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
        self.walls[direction] = False
        next_cell.walls[opposition_direction[direction]]=False

    def get_neighbors(self, n: int):
        neighbors = []
        if self.pos[0] > 0:
            neighbors.append(((self.pos[0]-1, self.pos[1]), 'N'))
        if self.pos[0] < n-1:
            neighbors.append(((self.pos[0]+1, self.pos[1]), 'S'))
        if self.pos[1] > 0:
            neighbors.append(((self.pos[0], self.pos[1]-1), 'W'))
        if self.pos[1] < n-1:
            neighbors.append(((self.pos[0], self.pos[1]+1), 'E'))
        return neighbors
    