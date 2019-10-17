#!/usr/bin/python3

from random import randrange

# Initialisation de la variable nombre_user à -1 pour éviter que le nombre aléatoire soit identique
nombre_user = -1

# Génération du nombre aléatoire
nombre_ordi = randrange(0, 100)

# Création de la variable 'help' pour réafficher le but du jeu
help = "oskour"

# Création de la variable 'exit' pour sortir du jeu
exit = "exit"

print ("C'est parti ! Affiche un nombre entier positif compris entre 0 et 100")

while nombre_user != nombre_ordi:
    nombre_user = input()

    # Affiche la règle du jeu
    if nombre_user == help:
        print("Tu dois trouver le bon nombre")
        continue

    # Arrête le jeu
    if nombre_user == exit:
        print("Tu abandonnes ? Lâche")
        break
    
    nombre_user = int(nombre_user)

    if nombre_user > nombre_ordi:
        print("C'est moins")

    elif nombre_user < nombre_ordi:
        print("C'est plus")

    else:
        print("GG WP")