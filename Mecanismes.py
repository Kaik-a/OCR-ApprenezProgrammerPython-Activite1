# -*- coding: utf-8 -*-

"""Ce fichier contient les principaux mécanismes du jeu Roboc""" 

from Robot import *
from Carte import *
import sys

def rules():
    """Afficher les règles du jeu"""
    print("\tLe jeu est un labyrinthe formé d'obstacles : des murs qui sont tout simplement là pour vous ralentir, des portes qui peuvent être traversées \n \
    et au moins un point par lequel on peut quitter le labyrinthe. Si le robot arrive sur ce point, la partie est considérée comme gagnée. \n \
    \n \
    Le robot est contrôlable grâce à des commandes entrées au clavier. Les commandes sont les suivantes :\n \
    Q permet de sauvegarder et quitter la partie en cours \n \
    N qui demande au robot de se déplacer vers le nord (c'est-à-dire le haut de votre écran) \n \
    E qui demande au robot de se déplacer vers l'est (c'est-à-dire la droite de votre écran) \n \
    S qui demande au robot de se déplacer vers le sud (c'est-à-dire le bas de votre écran) \n \
    O qui demande au robot de se déplacer vers l'ouest (c'est-à-dire la gauche de votre écran) \n \
    Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 pour avancer de trois cases vers l'est).\n \
    \n \
    Les murs sont représentés par des 'O' \n \
    Les portes sont représentées par des '.' \n \
    La sortie est représentée par un 'U' \n \
    Le robot est représenté par un 'X' ")
    
def  win():
    """Afficher le message de victoire et relancer le jeu"""
    print("Roboc est sauvé !!!")
    roboc()
    
def move():
    """"On détermine le mouvement à appliquer par rapport à l'entrée utilisateur"""
    multiplicateur = 1
    direction = ""
    valide = False
    
    while valide == False:
        orientation = input("Où allons nous ?")
        orientation = orientation.lower()
        if len(orientation) == 1 and orientation[0] in ["o", "e", "s", "n", "q"]: #si une seule entrée on vérifie qu'elle fasse partie des paramètres autorisés
            valide = True
            direction = orientation[0] 
        elif len(orientation) == 2 and orientation[0] in ["o", "e", "s", "n"] and orientation[1] in("0123456789"): #idem si deux entrées
            direction = orientation[0]
            multiplicateur = int(orientation[1])
            valide = True
        else:
            print("La commande est incorrecte")
    
    vecteur = (0,0) #On créé un vecteur pour matérialiser le déplacement
    if direction == "n":
        vecteur = (-1 * multiplicateur, 0)
    elif direction == "s":
        vecteur = (1 * multiplicateur, 0)
    elif direction == "e":
        vecteur = (0, 1 * multiplicateur)
    elif direction == "o":
        vecteur = (0, -1 * multiplicateur)
    elif direction == "q":
        vecteur = "q"
        
    return vecteur
        

def quit_save(txt):
    """Quitter et sauvegarder"""
    map_save("carte_en_cours.txt", txt)
    print("Vous quittez votre partie et celle-ci est sauvregardée")
    sys.exit()
    
def play(carteCopie, carteOriginale):
    """Lancer le jeu"""
    deplacement = move()
    posRobot = get_position(carteCopie)
    
    if deplacement != "q": 
        condition = move_to(carteCopie, posRobot, deplacement)
    else:
        quit_save(map_generate(carteCopie))
        
    if condition != posRobot: 
        carteCopie[condition] = "X" 
        carteCopie[posRobot] = carteOriginale[posRobot]
    print(map_generate(carteCopie))
    if carteOriginale[condition] == "U":
        win()

def begin():
    """"Initialisation du jeu"""
    rules()
    listCarte = map_list()
    carte_en_cours = "carte_en_cours"
    if carte_en_cours in listCarte:
        del listCarte[0]
        valable = False
        while valable == False:
            answer = input("Charger la partie en cours? (O/N)")
            answer = answer.lower()
            if answer in ["o", "n"]:
                valable = True
                if answer == "o":
                    return carte_en_cours + ".txt"
            else:
                print("Commande invalide!")
    print("Choisissez une carte :")
    listCarte2 = []
    for index, name in enumerate(listCarte):
        listCarte2.append(str(index))
        print("'{}' => Carte '{}'".format(index, name))
    valable = False
    while valable == False: 
        answer = (input(""))
        if answer in listCarte2:
            valable = True
            
            return listCarte[int(answer)] + ".txt"
        else:
            print("La carte choisie est incorrecte, vérifiez votre saisie")

def roboc():
    """Fonction principale"""
    maze = begin()
    
    carteOriginale = {}
    carteCopie = {}
    
    if type(maze) == str: 
        carteOriginale = map_dict(maze)
        carteCopie = map_dict(maze)
    else:
        carteOriginale = maze.copy()
        carteCopie = maze.copy()
        
    posRobot = get_position(carteOriginale)
    carteOriginale[posRobot] = " "
    
    print(map_generate(carteCopie))
    while True: 
        game = play(carteCopie, carteOriginale)
    quit_save(game)
    