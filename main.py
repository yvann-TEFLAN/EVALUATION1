#---------EXERCICE 1--------#
"""extraire l'ensemble des voyelles"""

from typing import AsyncGenerator


def extrait_ensemble_voyelles():
    mot="quelconque"
    while mot !="fin":
        mot= input("rentrez un mot(sans accent):")
#on met toutes les lettres en miniscule 
        mot_min= mot.lower()
#on crée la liste des voyelles
        liste_voyelles="a","e","i","o","u","y"

#on initialise le compteur de voyelles
        nb_voyelles= 0

#la boucle de comptage
        for lettre in mot_min:
          if lettre in liste_voyelles:
            nb_voyelles +=1

#l'affichage des résultats
        if nb_voyelles==0:
          return ("il n'y a pas de voyelles dans le mot\" +mot+""\".\n")
        elif nb_voyelles==1:
          return ("il y a une seule voyelle dans le mot\" +mot+""\".\n")
        else:
          return("n\n")
          return nb_voyelles.lower()
    #input("appuyer sur entrer pour terminer le programme")

#exercice2
def transforme_en_numeros(mot):
   
    if len(age) != 1:
        return 0
    new = ord(age)
    if 65 <= new <= 90:
        # Lettre majuscule
        return new - 64
    elif 97 <= new <= 122:
        # letter miniscule
        return new - 96
    # caractère méconnu
    return 0
#exercice 3

def contenu_cellule(colonne, ligne, univers):
  pass


