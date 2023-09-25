from classes.Cell import Cell
import random
import os

class Labyrinthe:
    def __init__(self, nom: str, n: int):
        self.nom = nom
        self.n = n
        self.grille = [[Cell((i, j)) for j in range(self.n)] for i in range(self.n)]
        self.entree = self.get_cellule(0, 0)
        self.ensembles = list(range(self.n * self.n))

    def get_cellule(self, x: int, y: int):
        return self.grille[x][y]

    def retour_arriere(self):
        cellule_courante = self.entree
        cellule_courante.visitee = True
        iteration = 0
        pile = [cellule_courante]
        while iteration < self.n * self.n:
            voisins = cellule_courante.obtenir_voisins(self.n)
            voisins_non_visites = [voisin for voisin in voisins if not self.get_cellule(voisin[0][0], voisin[0][1]).visitee]
            if voisins_non_visites:
                voisin_aleatoire = random.choice(voisins_non_visites)
                cellule_suivante = self.get_cellule(voisin_aleatoire[0][0], voisin_aleatoire[0][1])
                direction = voisin_aleatoire[1]
                cellule_suivante.visitee = True
                cellule_courante.casser_mur(cellule_suivante, direction)
                pile.append(cellule_suivante)
                cellule_courante = cellule_suivante
            else:
                if pile:
                    cellule_courante = pile.pop()
                    iteration -= 1
                iteration += 1

    def kruskal(self):
        aretes = []
        for ligne in range(self.n):
            for colonne in range(self.n):
                cellule = self.grille[ligne][colonne]
                voisins = cellule.obtenir_voisins(self.n)
                for voisin, direction in voisins:
                    aretes.append((cellule, self.get_cellule(voisin[0], voisin[1]), direction))
        random.shuffle(aretes)
        for arete in aretes:
            cellule1, cellule2, direction = arete
            ensemble1 = self.ensembles[cellule1.pos[0] * self.n + cellule1.pos[1]]
            ensemble2 = self.ensembles[cellule2.pos[0] * self.n + cellule2.pos[1]]
            if ensemble1 != ensemble2:
                ensemble_min = min(ensemble1, ensemble2)
                ensemble_max = max(ensemble1, ensemble2)
                for i in range(self.n * self.n):
                    if self.ensembles[i] == ensemble_max:
                        self.ensembles[i] = ensemble_min
                cellule1.casser_mur(cellule2, direction)
                cellule1.visitee = True
                cellule2.visitee = True

    def afficher_labyrinthe(self):
        labyrinthe_affiche = [["#" for _ in range(2 * self.n + 1)] for _ in range(2 * self.n + 1)]
        for ligne in range(self.n):
            for colonne in range(self.n):
                if self.grille[ligne][colonne].visitee:
                    labyrinthe_affiche[2 * ligne + 1][2 * colonne + 1] = "."
                if self.grille[ligne][colonne].murs['N']:
                    labyrinthe_affiche[2 * ligne][2 * colonne + 1] = "#"
                else:
                    labyrinthe_affiche[2 * ligne][2 * colonne + 1] = "."
                if self.grille[ligne][colonne].murs['S']:
                    labyrinthe_affiche[2 * ligne + 2][2 * colonne + 1] = "#"
                else:
                    labyrinthe_affiche[2 * ligne + 2][2 * colonne + 1] = "."
                if self.grille[ligne][colonne].murs['O']:
                    labyrinthe_affiche[2 * ligne + 1][2 * colonne] = "#"
                else:
                    labyrinthe_affiche[2 * ligne + 1][2 * colonne] = "."
                if self.grille[ligne][colonne].murs['E']:
                    labyrinthe_affiche[2 * ligne + 1][2 * colonne + 2] = "#"
                else:
                    labyrinthe_affiche[2 * ligne + 1][2 * colonne + 2] = "."
        labyrinthe_affiche[0][0] = "."
        labyrinthe_affiche[1][0] = "."
        labyrinthe_affiche[2 * self.n][2 * self.n] = "."
        labyrinthe_affiche[2 * self.n - 1][2 * self.n] = "."
        labyrinthe_str = ""
        count = 0
        for ligne in labyrinthe_affiche:
            if count == len(labyrinthe_affiche) - 1:
                labyrinthe_str += "".join(ligne)
            else:
                labyrinthe_str += "".join(ligne) + '\n'
            count += 1
        return labyrinthe_str

    def enregistrer_fichier(self, nom: str, texte_labyrinthe: str, generation: str):
        dossier_labyrinthe = './generateur/labyrinthe_genere/' + generation
        nom_avec_tirets = nom.replace(' ', '_')
        if not os.path.exists(dossier_labyrinthe):
            os.makedirs(dossier_labyrinthe)
        nom_fichier = os.path.join(dossier_labyrinthe, f'{nom_avec_tirets}.txt')
        with open(nom_fichier, 'w') as fichier:
            fichier.write(texte_labyrinthe)
        print(f'Le labyrinthe a été enregistré sous le nom {nom_fichier}')
