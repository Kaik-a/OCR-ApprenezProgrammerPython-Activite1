# -*- coding: utf-8 -*-
"""Ce fichier contient la classe carte ainsi que les fonctions nécessaires \
 à l'enregistrement, création et uilisation de cartes """


class Map:

    @staticmethod
    def map_list():
        """On récupère la liste des fichiers *.txt contenus dans le répertoire cartes"""
        import glob 
        maplist = glob.glob("cartes/*.txt")
        
        for index, name in enumerate(maplist):
            backslash = name.rfind("\\")
            maplist[index] = name[backslash + 1: -4]  # On récupère à partir du nom du fichier uniquement ce qui se /
            # situe après le backSlash et avant .txt
        return maplist

    @staticmethod
    def map_save(file, txt):
        """Enregistrer carte"""
        with open("cartes/" + file, "w") as fichier:
            fichier.write(txt)
        print("Partie enregistrée")

    @staticmethod
    def map_dict(file):
        d = {}
        with open("cartes/"+file, "r") as f:
            for i, l in enumerate(f):  # On créé la carte sous forme de dictionnaire  /
                # [(coordonnes x, coodonnees y)] = parametre
                for j in range(len(l)):
                    if l[j] in {"O", "X", " ", "U", "."}:
                        d[(i, j)] = l[j]
            return d

    @staticmethod
    def map_generate(d):
        """Générer carte à partir de dictionnaire"""
        carte = ""
        
        alimentation = d.keys()
        
        nblignecol = list(map(max, zip(*alimentation)))
        
        for i in range(nblignecol[0] + 1):
            for j in range(nblignecol[1] + 1):
                element = d[(i, j)] 
                carte += element 
            carte += "\n"
        
        return carte
