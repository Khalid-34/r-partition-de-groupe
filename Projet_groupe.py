from random import *
import json

#nom_du_fichier =input("selectionner du fichier: ")
#nombre_max_groupe =input("entre un chiffre: ")

fichier_nom = open('promo.txt' ,"r" ,encoding= 'utf8')
fichier_nom = fichier_nom.readlines()

nombre = len(fichier_nom)
print(nombre,"personnes")

shuffle(fichier_nom)
#print(fichier_nom)

i=0
while 0 < nombre:
    try:
        groupe = sample(nombre, 4)
        print(f"Groupe n°{i+1} : {groupe}")
        i +=1
        for nom in groupe:
           fichier_nom.remove(nom)
    except:
        break
    nombre += 1
print(f"Groupe n°{i+1} : {fichier_nom}")







#for i in fichier_nom:
    #i = sample(fichier_nom, 3)
    #fichier_nom.remove(i)
    #print(i)