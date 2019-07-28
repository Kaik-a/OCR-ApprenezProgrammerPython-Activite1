# -*- coding: utf-8 -*-

"""Ce fichier contient les principaux mécanismes du jeu Roboc""" 

from Robot import *
from Carte import *
import sys
import time

walle = Robot("Wall-E")
carte = Map()


def rules():
    """Afficher les règles du jeu"""
    print("\tLe jeu est un labyrinthe formé d'obstacles : des murs qui sont tout simplement là pour vous ralentir, \
des portes qui peuvent être traversées\n \
    et au moins un point par lequel on peut quitter le labyrinthe. Si le robot arrive sur ce point, la partie est\
considérée comme gagnée. \n \
    \n \
    Le robot est contrôlable grâce à des commandes entrées au clavier. Les commandes sont les suivantes :\n \
    Q permet de sauvegarder et quitter la partie en cours \n \
    N qui demande au robot de se déplacer vers le nord (c'est-à-dire le haut de votre écran) \n \
    E qui demande au robot de se déplacer vers l'est (c'est-à-dire la droite de votre écran) \n \
    S qui demande au robot de se déplacer vers le sud (c'est-à-dire le bas de votre écran) \n \
    O qui demande au robot de se déplacer vers l'ouest (c'est-à-dire la gauche de votre écran) \n \
    Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 \
    pour avancer de trois cases vers l'est).\n \
    M permet de murer la porte dans la direction indiquée (MS murera ainsi la porte au sud) \n \
    P permet de percer une porte dans le mur de la direction indiquée \n \
    \n \
    Les murs sont représentés par des 'O' \n \
    Les portes sont représentées par des '.' \n \
    La sortie est représentée par un 'U' \n \
    Le robot est représenté par un 'X' ")


def win():
    """Afficher le message de victoire et relancer le jeu"""
    print("{0} est sauvé !!!".format(walle.nom))
    roboc()


def ordres():
    """"On détermine le mouvement à appliquer par rapport à l'entrée utilisateur"""
    multiplicateur = 1
    vecteur = (0, 0)  # On créé un vecteur pour matérialiser le déplacement
    direction = ""
    commande = ""
    valide = False
    
    while valide is False:
        ordre = input("Quelle action souhaitez-vous réaliser ?")
        ordre = ordre.lower()
        
        if len(ordre) == 1 and ordre[0] in ["o", "e", "s", "n", "q"]:  # si une seule entrée on vérifie qu'elle fasse /
            # partie des paramètres autorisés
            if ordre[0] == "q":
                commande = "q"
            else:
                direction = ordre[0] 
            valide = True
        elif len(ordre) == 2 and ordre[0] in ["o", "e", "s", "n"] and ordre[1] in "0123456789":  # idem si deux entrées
            direction = ordre[0]
            multiplicateur = int(ordre[1])
            valide = True
        elif len(ordre) == 2 and ordre[1] in ["o", "e", "s", "n"] and ordre[0] == "m" or ordre[0] == "p":
            # Si on souhaite murer une porte
            direction = ordre[1]
            if ordre[0] == "m":
                commande = "m"  
            elif ordre[0] == "p":
                commande = "p"
            valide = True
        elif len(ordre) == 3 and ordre[0] in ["o", "e", "s", "n"] and ordre[1] in "12345679" \
                and ordre[2] in "012345679":
            direction = ordre[0]
            multiplicateur = int(ordre[1] + ordre[2])
            valide = True
        else:
            print("La commande est incorrecte, veuillez recommencer")
            return ordres()

    if direction == "n":
        vecteur = (-1 * multiplicateur, 0)
    elif direction == "s":
        vecteur = (1 * multiplicateur, 0)
    elif direction == "e":
        vecteur = (0, 1 * multiplicateur)
    elif direction == "o":
        vecteur = (0, -1 * multiplicateur)
   
    return vecteur, commande
        

def quit_save(txt):
    """Quitter et sauvegarder"""
    carte.map_save("carte_en_cours.txt", txt)
    print("Vous quittez votre partie et celle-ci est sauvregardée")
    sys.exit()


def play(cartecopie, carteoriginale):
    """Lancer le jeu"""
    
    deplacement, ordre = ordres()
    
    if ordre == "q": 
        print("Au revoir !")
        time.sleep(3)
        sys.exit()
    elif ordre == "m":
        condition = walle.murer(cartecopie, deplacement)
    elif ordre == "p":
        condition = walle.percer(cartecopie, deplacement)
    else:
        condition = walle.move_to(cartecopie, carteoriginale, deplacement)
        
    # if condition != walle.position:
    # cartecopie[condition] = "X"
    #    cartecopie[walle.position] = "X"
        
    print(carte.map_generate(cartecopie))
    if carteoriginale[condition] == "U":
        win()


def begin():
    """"Initialisation du jeu"""
    rules()
    listcarte = carte.map_list()
    carte_en_cours = "carte_en_cours"
    if carte_en_cours in listcarte:
        del listcarte[0]
        valable = False

        while valable is False:
            answer = input("Charger la partie en cours? (O/N)")
            answer = answer.lower()

            if answer in ["o", "n"]:
                valable = True

                if answer == "o":
                    return carte_en_cours + ".txt"
            else:
                print("Commande invalide!")

    print("Choisissez une carte ou appuyer sur \"Q\" pour quitter:")
    listcarte2 = []

    for index, name in enumerate(listcarte):
        listcarte2.append(str(index))
        print("'{}' => Carte '{}'".format(index, name))
    valable = False

    while valable is False:
        answer = (input(""))
        answer = answer.lower()
        if answer in listcarte2:
            return listcarte[int(answer)] + ".txt"
        elif answer == "q":
            print("Au revoir !")
            time.sleep(3)
            sys.exit()
        else:
            print("La carte choisie est incorrecte, vérifiez votre saisie")


def roboc():
    """Fonction principale"""
    maze = begin()
    
    if type(maze) == str: 
        carteoriginale = carte.map_dict(maze)
        cartecopie = carte.map_dict(maze)
    else:
        carteoriginale = maze.copy()
        cartecopie = maze.copy()
        
    posrobot = walle.set_position(carteoriginale)
    print(posrobot)  # test
    print("la position de {0} est : {1}".format(walle.nom, walle.position))
    cartecopie[posrobot] = "X"
    
    print(carte.map_generate(cartecopie))
    while True: 
        play(cartecopie, carteoriginale)
