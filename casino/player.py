class Joueur:
    def __init__(self, nom, solde, historique=[]):
        self.nom = nom
        self.solde = solde
        self.historique = historique

    def __str__(self):
        return f"Joueur: {self.nom}, Solde: {self.solde}, Historique: {self.historique}"

    def add_history(self, entry):
        # entry est un dictionnaire (roulette, dépôt, retrait, etc.).
        self.historique.append(entry)
        print(f"Historique mis à jour: {entry}")

    def show_history(self):
        print("Historique des jeux:")
        for entry in self.historique:
            print(f"- {entry}")
