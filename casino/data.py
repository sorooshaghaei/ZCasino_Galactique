import json
import os
from player import Player

def save_player_json(player):
    data = {
        "name": player.name,
        "balance": player.balance,
        "history": player.history
    }
    with open(f"{player.name}.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Game saved for {player.name}!")


def load_player_json(name):
    filename = f"{name}.json"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
        player = Player(data["name"], data["balance"], data["history"])
        print(f"Welcome back, {player.name}!")
        return player
    else:
        print(f"No previous game found for {name}. Starting a new game.")
        return None
