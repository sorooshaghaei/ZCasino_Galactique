import random


def play_roulette(player):
    print(f"Bienvenue à la roulette, {player.nom}!")
    # Logique de jeu de roulette ici
    while True:
        # demande la mise
        try:
            mise = int(
                input(
                    f"Combien voulez-vous miser? Votre solde actuel est {player.solde}: "
                )
            )
        except ValueError:
            print("Mise invalide! Essayez à nouveau.")
            continue
        if mise > player.solde or mise <= 0:
            print("Mise invalide! Essayez à nouveau.")
            continue

        # demande le numéro choisi
        try:
            numero = int(input("Choisissez un numéro entre 0 et 36: "))
        except ValueError:
            print("Numéro invalide! Essayez à nouveau.")
            continue
        if numero < 0 or numero > 36:
            print("Numéro invalide! Essayez à nouveau.")
            continue

        # génère un nombre aléatoire
        resultat = random.randint(0, 36)
        print(f"Le résultat est: {resultat}")

        # calcule le gain/perte
        if resultat == numero:
            gain = mise * 35
            player.solde += gain
            print(
                f"Félicitations {player.nom}, vous avez gagné {gain}! "
                f"Votre solde actuel est {player.solde}."
            )
        else:
            gain = -mise
            player.solde += gain
            print(
                f"Désolé {player.nom}, vous avez perdu {mise}! "
                f"Votre solde actuel est {player.solde}."
            )

        # ajoute une entrée complète dans l’historique
        player.historique.append(
            {
                "jeu": "roulette",
                "mise": mise,
                "choix": numero,
                "résultat": resultat,
                "gain": gain,
                "solde_final": player.solde,
            }
        )

        # demande si le joueur veut rejouer
        rejouer = input("Voulez-vous rejouer? (y/n): ")
        if rejouer.lower() != "y":
            break

    # affiche l’historique complet
    print("\nVoici votre historique de jeu:")
    for entry in player.historique:
        print(
            f"- Mise {entry['mise']} sur {entry['choix']} "
            f"→ Résultat {entry['résultat']} "
            f"→ Gain {entry['gain']} | Solde: {entry['solde_final']}"
        )

    print("\nMerci d'avoir joué à la roulette!")
