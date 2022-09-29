""" Le but de la partie est d’accumuler le plus possible de victoires.  Elles s’additionnent en vainquant des monstres.
  Un personnage circule dans un couloir (le monde), à chaque extrémité du couloir il y a une porte.
   Chacune de ces portes mène à une salle (le niveau).
   Dans chaque salle, il y a un monstre et chaque monstre a un niveau de difficulté qui lui est propre.
"""
import random

niveau_vie = 20
force_adversaire = random.randint(1, 5)


def quiter():
    print("Merci et au revoir...")


def regle_du_jeux():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
          "  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire."
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de "
          "l’adversaire. "
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire."
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0."
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité "
          "de 1 point de vie.")


def menu():
    print("1- Combattre cet adversaire"
          "2- Contourner cet adversaire et aller ouvrir une autre"
          "3- Afficher les règles du jeu"
          "4- Quitter la partie")


while True:
    choix = int(input("Que voulez-vous faire ?"))
    if choix == 1:
        pass

    elif choix == 2:
        pass
    elif choix == 3:
        regle_du_jeux()
        continue

    elif choix == 4:
        quiter()
        break
    else:
        print(";-;")
