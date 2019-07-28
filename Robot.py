# -*- coding: utf-8 -*-
from Mecanismes import *
import random

"""Ce fichier contient la classe Robot"""
murperce = []


class Robot:

    def __init__(self, nom):
        self.nom = nom
        self.position = (0, 0)

    def set_position(self, labyrinthe):
        """On trouve un emplacement aléatoire dans le labyrinthe"""
        listelibre = []
        listeitems = labyrinthe.items()
        for item in listeitems:
            if item[1] == " ":
                listelibre.append(item[0])
        pos = random.choice(listelibre)
        self.position = pos
        return pos

    def move_to(self, d, carteoriginale, orientation):
        """Déplacement du robot si possible"""
        trajectoire = []
        depart = self.position
        allowed = True
        for a in range(orientation[0] + 1): 
            for b in range(orientation[1] + 1):
                trajectoire.append((self.position[0] + a, self.position[1] + b))
        dest = (self.position[0]+orientation[0], self.position[1]+orientation[1])  # variable destination finale
        for i in trajectoire:
            if i in d.keys() and d[i] == "O":  # On vérifie que le déplacement ne soit pas hors carte /
                # et qu'il n'y ait pas de murs
                allowed = False
        if dest in d.keys() and d[dest] != "O" and allowed:
            self.position = dest
            if depart in murperce:
                d[depart] = "."
            else:
                d[depart] = carteoriginale[depart]
            d[dest] = "X"
            return dest
        else:
            print("Vous ne pouvez pas réaliser ce déplacement")
            self.position = depart
            return self.position

    def murer(self, d, direction):
        
        amurer = (self.position[0]+direction[0], self.position[1]+direction[1])
        
        if amurer in d.keys() and d[amurer] == ".":  # On vérifie qu'il existe bien une porte à l'emplacement indiqué
            if amurer in murperce:
                murperce.remove(amurer)
            d[amurer] = "O"
            print("La porte a été correctement murée")
            return self.position
        else:
            print("il n'y à pas de porte à murer dans cette direction")
            return self.position

    def percer(self, d, direction):
        
        apercer = (self.position[0]+direction[0], self.position[1]+direction[1])

        if apercer in d.keys() and d[apercer] == "O":  # on vérifie qu'il existe bien une porte à l'emplacement /
            # indiqué J"ai voulu codé le fait qu'on pouvait pas percer un mur des bors mais je n'ai pas trouvé. /
            # Et comme c'est pas demandé =)... Par contre si vous avez une idée je suis preneur.
            d[apercer] = "."
            print("Une porte à été percée dans le mur")
            murperce.append(apercer)
            return self.position
        else:
            print("Vous ne pouvez pas percer cela")
            return self.position
