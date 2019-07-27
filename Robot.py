# -*- coding: utf-8 -*-
from Mecanismes import *

"""Ce fichier contient la classe Robot"""


class Robot:

    def __init__(self, nom):
        self.nom = nom

    @staticmethod
    def get_position(labyrinthe):
        """récupérer la position du robot"""
        for index, value in labyrinthe.items():
            if value == "X":
                return index  # On recherche la position du robot dans la carte

    @staticmethod
    def move_to(d, position, orientation):
        """Déplacement du robot si possible"""
        trajectoire = []
        allowed = True
        for a in range(orientation[0] + 1): 
            for b in range(orientation[1] + 1):
                trajectoire.append((position[0] + a, position[1] + b))
        dest = (position[0]+orientation[0], position[1]+orientation[1])  # On met en variable la destination finale
        for i in trajectoire:
            if i in d.keys() and d[i] == "O":  # On vérifie que le déplacement ne soit pas hors carte /
                # et qu'il n'y ait pas de murs
                allowed = False
        if dest in d.keys() and d[dest] != "O" and allowed:
            return dest
        else:
            print("Vous ne pouvez pas réaliser ce déplacement")
            return position

    @staticmethod
    def murer(d, position, direction):
        
        amurer = (position[0]+direction[0], position[1]+direction[1])
        
        if amurer in d.keys() and d[amurer] == ".":  # On vérifie qu'il existe bien une porte à l'emplacement indiqué
            d[amurer] = "O"
            print("La porte a été correctement murée")
            return position
        else:
            print("il n'y à pas de porte à murer dans cette direction")
            return position

    @staticmethod
    def percer(d, position, direction):
        
        apercer = (position[0]+direction[0], position[1]+direction[1])
        
        if apercer in d.keys() and d[apercer] == "O":  # on vérifie qu'il existe bien une porte à l'emplacement /
            # indiqué J"ai voulu codé le fait qu'on pouvait pas percer un mur des bors mais je n'ai pas trouvé. /
            # Et comme c'est pas demandé =)... Par contre si vous avez une idée je suis preneur.
            d[apercer] = "."
            print("Une porte à été percée dans le mur")
            return position
        else:
            print("Vous ne pouvez pas percer cela")
            return position
