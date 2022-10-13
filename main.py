"""
Le but de la partie est d’accumuler le plus possible de victoires.  Elles s’additionnent en vainquant des monstres.
 Un personnage circule dans un couloir (le monde), à chaque extrémité du couloir il y a une porte.
  Chacune de ces portes mène à une salle (le niveau).
  Dans chaque salle, il y a un monstre et chaque monstre a un niveau de difficulté qui lui est propre.
"""
import random


def apparaitre_stat():
    print(f"numero de l'adversaire :{numero_adversaire}\n"
          f"Niveau de vie:_{niveau_vie}\n"
          f"Combat {numero_combat} :_nombre de victoire: {nombre_victoires} vs nombre de defait: {nombre_defaites}\n")


def quiter():
    print("Merci et au revoir...")


def apparaitre_regle_du_jeux():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
          "  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
          "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de\n "
          "l’adversaire.\n "
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité \n"
          "de 1 point de vie.\n"
          "l’adversaire.\n "
          "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
          "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
          "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité\n "
          "de 1 point de vie.\n")


def choix_du_joueur():
    global choix
    choix = int(input("1- Combattre cet adversair\n"
                      "2- Contourner cet adversaire et aller ouvrir une autre\n"
                      "3- Afficher les règles du jeu\n"
                      "4- Quitter la partie\n"
                      ""))


play_game = True
while play_game:
    choix = 0
    niveau_vie = 20
    numero_adversaire = 0
    numero_combat = 0
    nombre_victoires = 0
    nombre_defaites = 0
    combat_statut = "aucune battaille efectuer encore pour le moment..."
    nombre_victoires_consecutives = 0
    afficher_regle = False
    force_adversaire = 0

    while niveau_vie > 0:
        if not afficher_regle:
            force_adversaire = random.randint(1, 5)
        else:
            afficher_regle = False

        print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaire}\n")
        choix_du_joueur()

        if choix == 1:
            numero_adversaire += 1
            numero_combat += 1
            apparaitre_stat()
            score_de = random.randint(1, 6)

            if force_adversaire >= score_de:
                print(f"force_adversaire:{force_adversaire}\n"
                      f"Lancer du dé : {score_de}")
                niveau_vie -= force_adversaire
                combat_statut = "defaites"
                nombre_defaites += 1
                nombre_victoires_consecutives = 0
                print(f"Dernier combat = {combat_statut}")
                print(f"Niveau de vie :{niveau_vie}\n")

            else:
                print(f"Lancer du dé : {score_de}")
                niveau_vie += force_adversaire
                nombre_victoires_consecutives += 1
                combat_statut = "victoire"
                nombre_victoires += 1
                print(f"Dernier combat = {combat_statut}")
                print(f"Niveau de vie : {niveau_vie} \n"
                      f"Nombre de victoires consécutives : {nombre_victoires_consecutives}\n")

        elif choix == 2:
            niveau_vie -= 1
            print("pénalité de 1 point de vie, vous avez reussi a contourner le monstre.\n")

        elif choix == 3:
            afficher_regle = True
            apparaitre_regle_du_jeux()

        elif choix == 4:
            quiter()
            play_game = False
            break

        else:
            print(";-;\n"
                  "silvous plait recomencer...\n")

    else:
        print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
