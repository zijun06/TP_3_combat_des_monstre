"""
Le but de la partie est d’accumuler le plus possible de victoires.  Elles s’additionnent en vainquant des monstres.
  Un personnage circule dans un couloir (le monde), à chaque extrémité du couloir il y a une porte.
   Chacune de ces portes mène à une salle (le niveau).
   Dans chaque salle, il y a un monstre et chaque monstre a un niveau de difficulté qui lui est propre.
"""
import random

niveau_vie = 20
score_de = random.randint(1, 6)
numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
combat_statut = "aucune battaille efectuer encore pour le moment..."

force_adversaire = random.randint(1, 5)


def apparaitre_stat():
    print(f"Adversaire :{numero_adversaire}\n"
          f"Force de l’adversaire :_{force_adversaire}\n"
          f"Niveau de vie de l’usager :_{niveau_vie}\n"
          f"Combat {numero_combat} :_{nombre_victoires} vs {nombre_defaites}\n"
          f"Lancer du de:_{score_de}\n"
          f"Dernier combat = {combat_statut}\n")
    str(input("espace pour continuer...\n"))


def quiter():
    print("Merci et au revoir...")


def apparaitre_regle_du_jeux():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
          "  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de "
          "l’adversaire.\n "
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité\n "
          "de 1 point de vie.\n")


def menu():
    print("1- Combattre cet adversair\n"
          "2- Contourner cet adversaire et aller ouvrir une autre\n"
          "3- Afficher les règles du jeu\n"
          "4- Quitter la partie\n")


while True:
    print(f"Vous tombez face à face avec un adversaire de difficulté :_{force_adversaire}\n")
    menu()
    choix = int(input("Que voulez-vous faire ?"))

    if choix == 1:
        apparaitre_stat()
        if force_adversaire >= score_de:
            niveau_vie -= force_adversaire
            combat_statut = "defaites"
            numero_adversaire += 1
            numero_combat += 1
            nombre_defaites += 1

            if niveau_vie <= 0:
                print()
        else:
            niveau_vie += force_adversaire
            combat_statut = "victoire"
            numero_adversaire += 1
            numero_combat += 1
            nombre_victoires += 1


    elif choix == 2:
        print("2")

    elif choix == 3:
        apparaitre_regle_du_jeux()

    elif choix == 4:
        quiter()
        break
    else:
        print(";-;\n"
              "silvous plait recomencer...\n")
