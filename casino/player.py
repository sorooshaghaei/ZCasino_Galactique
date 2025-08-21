# player.py
class Player:
    def __init__(self, name, balance, history=None):
        self.name = name
        self.balance = balance
        self.history = history if history is not None else []

    def __str__(self):
        return f"Player: {self.name}, Balance: {self.balance}, History: {self.history}"

    def add_history(self, entry):
        # entry is a dictionary (roulette, deposit, withdrawal, etc.)
        self.history.append(entry)
        print(f"History updated: {entry}")

    def show_history(self):
        print("Game History:")
        if not self.history:
            print("- No history yet.")
        for entry in self.history:
            print(f"- {entry}")