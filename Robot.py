# -*- coding: utf-8 -*-

"""Ce fichier contient la classe Robot"""
 
class Robot():

    def get_position(self, carte):
        """récupérer la position du robot"""
        for index, value in carte.items(): 
            if value == "X":
                return index #On recherche la position du robot dans la carte
        
    def  move_to(self, d, position, orientation):
        """Déplacement du robot si possible"""
        trajectoire = []
        allowed = True
        for a in range(orientation[0] + 1): 
            for b in range(orientation[1] + 1):
                trajectoire.append((position[0] + a, position[1] + b))
        dest = (position[0]+orientation[0],position[1]+orientation[1]) #On met en variable la destination finale
        for i in trajectoire:
            if i in d.keys() and d[i] == "O": #On vérifie que le déplacement ne soit pas hors carte et qu'il n'y ait pas de murs
                allowed = False
        if dest in d.keys() and d[dest] != "O" and allowed:
            return dest
        else:
            print("Vous ne pouvez pas réaliser ce déplacement")
            return position
                    