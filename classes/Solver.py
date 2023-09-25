import os
from PIL import Image

class Solveur:
    def __init__(self, plateau: list):
        self.plateau = plateau
        self.visite = False
        self.depart, self.arrivee = self.obtenir_points_depart_arrivee()
        self.pile = [self.depart]
        
    def obtenir_points_depart_arrivee(self):
        _depart = [i for i in range(len(self.plateau[0])) if self.plateau[0][i] == '.']
        _arrivee = [i for i in range(len(self.plateau[0])) if self.plateau[len(self.plateau)-1][i] == '.']
        return [0, _depart[0]], [len(self.plateau) - 1, _arrivee[0]]

    def solveur_retour_arriere(self):
        self.plateau[self.depart[0]][self.depart[1]] = 'o'
        self.remonter()

    def remonter(self):
        while self.pile:
            cellule_courante = self.pile[-1]
            if cellule_courante == self.arrivee:
                return
            deplace = False
            if cellule_courante[0] + 1 < len(self.plateau) and self.plateau[cellule_courante[0] + 1][cellule_courante[1]] == '.':
                self.plateau[cellule_courante[0] + 1][cellule_courante[1]] = 'o'
                self.pile.append([cellule_courante[0] + 1, cellule_courante[1]])
                deplace = True
            elif cellule_courante[1] + 1 < len(self.plateau[0]) and self.plateau[cellule_courante[0]][cellule_courante[1] + 1] == '.':
                self.plateau[cellule_courante[0]][cellule_courante[1] + 1] = 'o'
                self.pile.append([cellule_courante[0], cellule_courante[1] + 1])
                deplace = True
            elif cellule_courante[0] - 1 >= 0 and self.plateau[cellule_courante[0] - 1][cellule_courante[1]] == '.':
                self.plateau[cellule_courante[0] - 1][cellule_courante[1]] = 'o'
                self.pile.append([cellule_courante[0] - 1, cellule_courante[1]])
                deplace = True
            elif cellule_courante[1] - 1 >= 0 and self.plateau[cellule_courante[0]][cellule_courante[1] - 1] == '.':
                self.plateau[cellule_courante[0]][cellule_courante[1] - 1] = 'o'
                self.pile.append([cellule_courante[0], cellule_courante[1] - 1])
                deplace = True
            if not deplace:
                cellule_a_retirer = self.pile.pop()
                self.plateau[cellule_a_retirer[0]][cellule_a_retirer[1]] = '*'

    def astar(self):
        pass 

    def afficher_plateau(self):
        plateau_str = ""
        for ligne in range(len(self.plateau)):
            plateau_str += "".join(self.plateau[ligne]) + '\n'
        return plateau_str

    def sauvegarder_image(self, generation: str):
        nom = input('Entrez le nom souhaité (sans extension) : ')
        if generation == "astar":
            pass
        elif generation == "retour_arriere":
            self.solveur_retour_arriere()
        
        texte_plateau = self.afficher_plateau()
        dossier_plateau = './solveur/plateau_resolu/' + generation
        nom_avec_tirets = nom.replace(' ', '_')
        
        if not os.path.exists(dossier_plateau):
            os.makedirs(dossier_plateau)
        
        nom_fichier_txt = os.path.join(dossier_plateau, f'{nom_avec_tirets}.txt')
        nom_fichier_jpg = os.path.join(dossier_plateau, f'{nom_avec_tirets}.jpg')
        
        with open(nom_fichier_txt, 'w') as fichier:
            fichier.write(texte_plateau)
        
        resolution_image = (len(self.plateau[0]) * 10, len(self.plateau) * 10)
        image_plateau = Image.new('RGB', resolution_image)
        for x in range(len(self.plateau[0])):
            for y in range(len(self.plateau)):
                if self.plateau[y][x] == '#':
                    image_plateau.paste((0, 0, 0), (x * 10, y * 10, (x + 1) * 10, (y + 1) * 10))
                elif self.plateau[y][x] == 'o':
                    image_plateau.paste((46, 139, 87), (x * 10, y * 10, (x + 1) * 10, (y + 1) * 10))
                elif self.plateau[y][x] == '*':
                    image_plateau.paste((255, 0, 0), (x * 10, y * 10, (x + 1) * 10, (y + 1) * 10))
                else:
                    image_plateau.paste((206, 206, 206), (x * 10, y * 10, (x + 1) * 10, (y + 1) * 10))

        image_plateau.save(nom_fichier_jpg, 'JPEG')
        print(f'Le plateau résolu a été enregistré sous le nom {nom_fichier_txt} et {nom_fichier_jpg}')

    def choisir_solveur(self):
        while True:
            print(' ')
            print("Choisissez un algorithme de résolution de labyrinthe")
            print("1 - Algorithme A*")
            print('2 - Algorithme de retour en arrière')
            print('3 - Quitter')
            print(' ')
            numero = input('Entrez un numéro > ')
            print(' ')
            if not numero.isdigit():
                print(' ')
                print('Entrez un numéro entre 1 et 2 !')
                print(' ')
            elif numero == "1":
                self.sauvegarder_image("astar")
                break
            elif numero == "2":
                self.sauvegarder_image("retour_arriere")
                break
            elif numero == "3":
                break
            else:
                print(' ')
                print('Entrez un numéro valide !')
                print(' ')
