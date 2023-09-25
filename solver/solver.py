import sys
import os

dossier_racine = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_racine)

from classes.Maze import *
from classes.Solver import *

def obtenir_generateur(generation: str):
    dossier = './generateur/labyrinthe_genere/' + generation
    nom = input("Entrez le nom du labyrinthe à résoudre : ")
    chemin_fichier = os.path.join(dossier, nom)
    if not chemin_fichier.endswith(".txt"):
        chemin_fichier += ".txt"
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read()
        lignes = contenu.split('\n')
        plateau = [list(ligne) for ligne in lignes]
        solveur = Solveur(plateau)
        solveur.choisir_solveur()
    else:
        print(f"Le fichier {chemin_fichier} n'existe pas.")

def demarrer():
    while True:
        print(' ')
        print("Choisissez la génération de votre labyrinthe")
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
            obtenir_generateur("kruskal")
        elif numero == "2":
            obtenir_generateur("retour_arriere")
        elif numero == "3":
            break
        else:
            print(' ')
            print('Entrez un numéro valide !')
            print(' ')

demarrer()
