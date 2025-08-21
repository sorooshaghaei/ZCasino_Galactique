from player import Player
from bank import deposit, withdraw
from roulette import play_roulette
from data import save_player_json, load_player_json

# Ask player name and try to load previous game
name = input("Enter your name: ")
player = load_player_json(name)
if player is None:
    player = Player(name, balance=1000)  # start new game

while True:
    action = input(
        f"""\nWhat do you want to do {player.name}?
1- Play Roulette
2- Make a deposit
3- Make a withdrawal
4- View history
5- Quit
Choose an option: """
    )

    if action == "1":
        play_roulette(player)
        save_player_json(player)  # save after game
    elif action == "2":
        try:
            amount = int(input("Enter the amount to deposit: "))
            deposit(player, amount)
            save_player_json(player)  # save after deposit
        except ValueError:
            print("Invalid amount! Try again.")
    elif action == "3":
        try:
            amount = int(input("Enter the amount to withdraw: "))
            withdraw(player, amount)
            save_player_json(player)  # save after withdrawal
        except ValueError:
            print("Invalid amount! Try again.")
    elif action == "4":
        player.show_history()
    elif action == "5":
        print("Thanks for playing!")
        save_player_json(player)  # save before exit
        break
    else:
        print("Invalid action! Try again.")
