import sys
import os

dossier_racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_racine)
from classes.Maze import *

def generer_labyrinthe(generation: str):
    nom = input('Entrez le nom souhaité (sans extension) : ')
    taille = int(input('Entrez une taille pour le labyrinthe : '))
    labyrinthe = Labyrinthe(nom, taille)
    if generation == "kruskal":
        labyrinthe.kruskal()
    elif generation == "retour_arriere":
        labyrinthe.retour_arriere()
    texte_labyrinthe = labyrinthe.afficher_labyrinthe()
    labyrinthe.enregistrer_fichier(nom, texte_labyrinthe, generation)

def demarrer():
    while True:
        print(' ')
        print("Choisissez un algorithme de génération de labyrinthe")
        print("1 - Algorithme de Kruskal")
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
            generer_labyrinthe("kruskal")
        elif numero == "2":
            generer_labyrinthe("retour_arriere")
        elif numero == "3":
            break
        else:
            print(' ')
            print('Entrez un numéro valide !')
            print(' ')

demarrer()
