from random import random


def play_roulette(player):
    print(f"Bienvenue à la roulette, {player.nom}!")
    # Logique de jeu de roulette ici
    while True:
        # demande la mise,
        mise = int(input(f"Combien voulez-vous miser? Votre solde actuel est {player.solde}."))
        if mise > player.solde or mise <= 0:
            print("Mise invalide! Essayez à nouveau.")
            continue
        # demande le numéro choisi,
        numero = int(input(f"Choisissez un numéro entre 0 et 36: "))
        if numero < 0 or numero > 36:
            print("Numéro invalide! Essayez à nouveau.")
            continue
        # génère un nombre aléatoire,
        resultat=random.randint(0,36)
        print(f"Le résultat est: {resultat}")

        # calcule le gain/perte,
        if resultat == numero:
            gain = mise * 35
            player.solde += gain
            print(f"Félicitation {player.nom}, vous avez gagné {gain}! Votre solde actuel est {player.solde}.")
            player.historique.append(("gain",gain))
        else:
            perte = mise
            player.solde -= perte
            print(f"Désolé {player.nom}, vous avez perdu {perte}! Votre solde actuel est {player.solde}.")
            player.historique.append(("perte",perte))
        
        
        











# enregistre le résultat dans l’historique.

