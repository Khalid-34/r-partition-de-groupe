from random import *
import json
import logging


#log = log.write("Début du log")
fichier = input("Veuillez entre le nom (ou chemin d'accès) du fichier : ")
nbgroup = int(input ("Entrer le nombre max de personne dans le groupe : "))

lecture = open(fichier, 'r', encoding='utf-8')
lecture = lecture.readlines()
shuffle(lecture)
liste = len(lecture)
i = 0
while 0 < liste:
    try:
        groupe = sample(lecture, nbgroup)
        print(f"Groupe n°{i+1} : {groupe}")
        i +=1
        for nom in groupe:
            lecture.remove(nom)
    except:
        break
    liste += 1
print(f"Groupe n°{i+1} : {lecture}")

# with open("Répartition des groupes.json", 'w', encoding='utf-8')