#!/usr/bin/python3

from statistics import mean

print("Entrez les notes.")

resultats = []

note = 0

while note != "":

    note = input("Votre note ")

    try:

        note = int(note)

        if note >= 0 and note <= 20:
            resultats.append(note)

        else:
            print("La note n'est pas comprise entre 0 et 20.")

    except ValueError:
        
        if note == "":
            continue

        else:
            print("Ce n'est pas une note.")
            pass

moyenne = mean(resultats)

moyenne = round(moyenne, 2)

resultat = sorted(resultats)

print("L'ensemble des notes croissantes : {0} et la moyenne est de {1}/20.".format(resultat, moyenne))