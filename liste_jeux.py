# Import du module sys :
import sys

# Déclaration des variables globales :
# Variable instructions :
MENU = """
MENU DES COMMANDES :
1 - Ajouter un jeu vidéo à votre liste
2 - Retirer un jeu vidéo à votre liste
3 - Afficher votre liste de jeux vidéos
4 - Supprimer la liste de jeux vidéos
5 - Sortir du programme
"""

# Variable options à sélectionner :
MENU_ITEMS = ["1", "2", "3", "4", "5"]

# Variables liste vide au départ :
LISTE = []

while True : 
    user_choice = ""
    while user_choice not in MENU_ITEMS:
        print(MENU)
        if user_choice not in MENU_ITEMS:
            user_choice = input("Votre choix de commande : ")
    
    if user_choice == "1":
        item = input("Ajoutez un jeu vidéo à votre liste : ")
        LISTE.append(item)
        print(f"--- Vous avez ajouté le jeu '{item}' à votre liste. ---")

    elif user_choice == "2":
        while True : 
            item = input("Retirer un jeu vidéo à votre liste : ")
            if item not in LISTE:
                print(f"Le jeu vidéo '{item}' n'est pas dans votre liste")   
            else:
                LISTE.remove(item)
                print(f"--- Vous avez retiré le jeu '{item}' à votre liste. ---")
                break
    
    elif user_choice == "3":
        if LISTE == []:
            print("--- Votre liste est vide ---")
        else:
            print("Voici votre liste de jeux vidéos :")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. --- {item} ---")

    elif user_choice == "4":
        if LISTE == []:
            print("--- Votre liste est déjà vide ---")
        else:
            LISTE.clear()
            print("--- Votre liste a bien été supprimée ---")

    elif user_choice == "5":
        print("--- Vous avez quitté le programme ---")
        sys.exit()

    print("- -" * 20)