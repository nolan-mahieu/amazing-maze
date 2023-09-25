class Cell():
    def __init__(self, pos: tuple):
        self.pos = pos
        self.walls = {"Haut": True, "Droite": True, "Bas": True, "Gauche": True}
        self.visited = False

    def casser_mur(self, cellule_suivante: 'Cell', direction: str):
        directions_opposees = {'Haut': 'Bas', 'Bas': 'Haut', 'Droite': 'Gauche', 'Gauche': 'Droite'}
        self.walls[direction] = False
        cellule_suivante.walls[directions_opposees[direction]] = False

    def obtenir_voisins(self, n: int):
        voisins = []
        if self.pos[0] > 0:
            voisins.append(((self.pos[0] - 1, self.pos[1]), 'Haut'))
        if self.pos[0] < n - 1:
            voisins.append(((self.pos[0] + 1, self.pos[1]), 'Bas'))
        if self.pos[1] > 0:
            voisins.append(((self.pos[0], self.pos[1] - 1), 'Gauche'))
        if self.pos[1] < n - 1:
            voisins.append(((self.pos[0], self.pos[1] + 1), 'Droite'))
        return voisins