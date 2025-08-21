def deposit(player, amount):
    player.solde += amount
    player.historique.append(
        {"type": "dépôt", "montant": amount, "solde": player.solde}
    )
    print(f"Vous avez déposé {amount}. Votre nouveau solde est {player.solde}.")


def withdraw(player, amount):
    if amount > player.solde or amount <= 0:
        print("Fonds insuffisants!")
    else:
        player.solde -= amount
        player.historique.append(
            {"type": "retrait", "montant": amount, "solde": player.solde}
        )
        print(f"Vous avez retiré {amount}. Votre nouveau solde est {player.solde}.")
